import sys

filename = r"c:\Users\uppro\Sync\O_Mar_26\ClaudeCode_CoWork_OS\SuperNotes_26\SuperNotes.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

target3 = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            padding: 8px;
            height: auto;
        }"""
repl3 = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            min-height: 0;
            padding: 8px;
            height: auto;
        }"""

if target3 in content:
    content = content.replace(target3, repl3)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacement successful.")
else:
    print("Target not found.")
