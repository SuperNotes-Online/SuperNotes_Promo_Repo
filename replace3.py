import sys

filename = r"c:\Users\uppro\Sync\O_Mar_26\ClaudeCode_CoWork_OS\SuperNotes_26\SuperNotes.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

target = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            min-height: 0;
            padding: 8px;
            height: auto;
        }"""
repl = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            overscroll-behavior: contain;
            min-height: 0;
            padding: 8px;
            height: 0;
        }"""

if target in content:
    content = content.replace(target, repl)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacement successful.")
else:
    print("Target not found.")
