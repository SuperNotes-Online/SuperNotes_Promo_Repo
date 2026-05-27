import sys
import re

with open('SuperNotes.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<div class="sidebar">([\s\S]*?)<div class="editor-pane">', text)
if match:
    content = match.group(1)
    tags = re.findall(r'<div class="([^"]+)"', content)
    print("Classes of divs inside sidebar before editor-pane:", tags[:15])
