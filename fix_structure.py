
import re

file_path = r'c:\Users\WD\Downloads\그룹웨어\그룹디2.0-2\package.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper function to fix a block
def fix_block(content, start_marker, end_marker):
    # 1. Fix Start: Close the parent card before the new card starts
    # Look for the marker (e.g. first inserted card's data-name)
    # Find the preceding "</div>" (CounterBox close) and insert another "</div>" (Card close) after it
    # Pattern: (</div>\s*)(<div class="card-dark ... marker ...)
    
    # We use the unique data-name of the FIRST inserted card in the block
    pattern_start = r'(</div>\s*)(<div class="card-dark[^>]*>\s*<div>\s*<span[^>]*>' + re.escape(start_marker)
    
    # Replacement: \1</div>\2
    # This adds a </div> before the Start Marker line, retaining whitespace
    
    # 2. Fix End: Remove the trailing parent closing div
    # Look for the marker (e.g. last inserted card's data-name)
    # Find its closing </div> (CountNum), then </div> (CounterBox), then </div> (Card).
    # Then the NEXT </div> is the one to remove.
    
    # This is tricky with regex. Let's do it in two passes.
    
    # Pass 1: Close parent
    # Find: `</div>\s*<div ... start_marker`
    # Replace: `</div></div>\n<div ...`
    
    # Use simple string search for robustness if possible, but regex handles whitespace.
    # We'll search for the unique "data-name" of the first card.
    start_str = f'data-name="{start_marker}"'
    start_idx = content.find(start_str)
    
    if start_idx == -1:
        print(f"Could not find start marker: {start_marker}")
        return content

    # Walk back to find `<div class="card-dark` start of this new card
    card_start_idx = content.rfind('<div class="card-dark', 0, start_idx)
    
    # Now check before card_start_idx if there is a </div>.
    # Using regex to find the whitespace gap
    # We want to replace the whitespace between `</div>` (previous counter) and `<div class="card-dark` (new card)
    # with `</div>\n<div class="card-dark`
    
    # Instead of walking back, let's use regex near the location.
    # Excerpt a chunk around card_start_idx
    chunk_start = max(0, card_start_idx - 100)
    chunk = content[chunk_start:card_start_idx]
    
    # We expect `</div>\s*` at the end of chunk.
    # We want to replace `</div>\s*$` with `</div></div>\n` + indent?
    
    # Let's perform a direct string replacement on the whole file using regex
    # Match: (</div>)(\s+)(<div class="card-dark"[^>]*>.*?data-name="MARKER")
    # Note: dotall to match across lines if needed, but the structure is usually clean
    
    regex_start = r'(</div>)(\s+)(<div class="card-dark"[^>]*>\s*<div>\s*<span[^>]*>[^<]*</span>\s*<span[^>]*>[^<]*</span>\s*</div>\s*<div class="counter-box">\s*<div[^>]*>.*?data-name="' + re.escape(start_marker) + r'")'
    
    # This regex is getting long and fragile.
    # Simpler: Find `<div class="card-dark` corresponding to the marker. Insert `</div>` before it.
    
    content = content[:card_start_idx] + "</div>" + content[card_start_idx:]
    
    # Now Pass 2: Remove trailing div
    # Find the end of the LAST card in the block.
    end_str = f'data-name="{end_marker}"'
    end_idx = content.find(end_str)
    
    if end_idx == -1:
        print(f"Could not find end marker: {end_marker}")
        return content # Warning: unbalanced if step 1 worked but 2 failed
        
    # Find closing of this end card.
    # It has `</div>` for CountNum, `</div>` for CounterBox, `</div>` for Card.
    # Scan forward from end_idx
    
    offset = end_idx
    for _ in range(3): # Find 3rd </div>
        offset = content.find('</div>', offset + 1)
        
    last_card_end = offset + 6 # After </div>
    
    # verify we are around where we think we are
    # check next non-whitespace char. It should be <
    # If the next tag is `</div>`, that's the one to delete.
    
    # Simple check: `content[last_card_end:].lstrip().startswith('</div>')`
    
    remaining = content[last_card_end:]
    stripped = remaining.lstrip()
    
    if stripped.startswith('</div>'):
        # Found the victim
        ws_len = len(remaining) - len(stripped)
        # Remove whitespace + </div>
        # Actually we might want to keep some newline?
        # Just remove the `</div>` and let formatting serve.
        # But we need to calculate exact position.
        
        victim_start = last_card_end + ws_len
        victim_end = victim_start + 6
        
        content = content[:victim_start] + content[victim_end:]
    else:
        print(f"Warning: Expected </div> after block {end_marker}, found {stripped[:10]}")
        
    return content

# Define blocks (Start Marker, End Marker)
# Start Marker: data-name of first new card
# End Marker: data-name of last new card
blocks = [
    ("광고: 파워링크 이미지", "광고: 카카오 비즈니스"),
    ("블로그: 프리미엄 브랜딩", "블로그: 프리미엄 브랜딩"), # Set 1 item
    ("블로그: 업로드 대행", "블로그: 서로이웃 관리"),
    ("영상: 셀프 숏폼", "영상: 셀프 숏폼"), # Set 1 item
    ("영상: 셀프 롱폼", "영상: 브랜딩 필름")
]

for start, end in blocks:
    content = fix_block(content, start, end)
    print(f"Fixed block: {start} -> {end}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
