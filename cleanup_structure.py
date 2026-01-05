
import re

file_path = r'c:\Users\WD\Downloads\그룹웨어\그룹디2.0-2\package.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def cleanup_ghosts(content, marker):
    # Find the marker
    str_marker = f'data-name="{marker}"'
    idx = content.find(str_marker)
    if idx == -1:
        print(f"Marker not found: {marker}")
        return content

    # Find the end of this card
    # 1. Close CountNum
    idx = content.find('</div>', idx) 
    # 2. Close CounterBox
    idx = content.find('</div>', idx + 1)
    # 3. Close Card
    idx = content.find('</div>', idx + 1)
    
    # idx points to the start of "</div>"
    card_end = idx + 6
    
    # Now look ahead
    # We want to remove any sequence of `\s*</div>` that follows immediately
    # We stop when we hit something that is NOT whitespace or </div>
    
    # Let's handle this by slicing
    stmba = content[card_end:] # suffix
    
    # Regex to find consecutive closing divs with whitespace
    # ^(\s*</div>)+
    
    match = re.match(r'^(\s*</div>)+', stmba)
    if match:
        print(f"Removing ghosts after {marker}: {match.group(0)}")
        # Remove the matched part
        content = content[:card_end] + stmba[match.end():]
    else:
        print(f"No ghosts found after {marker}")
        
    return content

markers = [
    "광고: 카카오 비즈니스",
    "블로그: 프리미엄 브랜딩",
    "블로그: 서로이웃 관리",
    "영상: 셀프 숏폼",
    "영상: 브랜딩 필름"
]

for m in markers:
    content = cleanup_ghosts(content, m)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
