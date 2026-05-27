import sys

filename = r"c:\Users\uppro\Sync\O_Mar_26\ClaudeCode_CoWork_OS\SuperNotes_26\SuperNotes.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

target1 = """        .filter-bar {
            padding: 10px 12px;
            border-bottom: 1px solid var(--border);
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            position: relative;
        }"""
repl1 = """        .filter-bar {
            padding: 10px 12px;
            border-bottom: 1px solid var(--border);
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            position: relative;
            flex-shrink: 0;
        }"""

target2 = """        .sort-bar {
            padding: 6px 12px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--surface2);
        }"""
repl2 = """        .sort-bar {
            padding: 6px 12px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--surface2);
            flex-shrink: 0;
        }"""

target3 = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            padding: 8px;
            height: 100%;
        }"""
repl3 = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            padding: 8px;
            height: auto;
        }"""

content = content.replace(target1, repl1)
content = content.replace(target2, repl2)
content = content.replace(target3, repl3)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement successful.")
