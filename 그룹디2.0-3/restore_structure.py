
import re

file_path = r'c:\Users\WD\Downloads\그룹웨어\그룹디2.0-2\package.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def restore_divs(content, marker, count):
    # Find the marker
    str_marker = f'data-name="{marker}"'
    idx = content.find(str_marker)
    if idx == -1:
        print(f"Marker not found: {marker}")
        return content

    # Find the end of this card
    # Close CountNum, CounterBox, Card
    idx = content.find('</div>', idx) 
    idx = content.find('</div>', idx + 1)
    idx = content.find('</div>', idx + 1)
    
    card_end = idx + 6
    
    # Insert 'count' divs
    divs = "\n" + ("    </div>\n" * count)
    
    content = content[:card_end] + divs + content[card_end:]
    print(f"Restored {count} divs after {marker}")
    return content

# Manuscript End: Neighbor Mgmt -> Needs 2 divs (space-y-4, mb-12)
content = restore_divs(content, "블로그: 서로이웃 관리", 2)

# Video End: Branding Film -> Needs 3 divs (space-y-4, mb-12, flex-col)
content = restore_divs(content, "영상: 브랜딩 필름", 3)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
