import sys

filename = r"c:\Users\uppro\Sync\O_Mar_26\ClaudeCode_CoWork_OS\SuperNotes_26\SuperNotes.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Base .sidebar
old_base_sidebar = """        .sidebar {
            width: 300px;
            flex-shrink: 0;
            background: var(--surface);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            min-height: 0;
        }"""
new_base_sidebar = """        .sidebar {
            width: 300px;
            flex-shrink: 0;
            background: var(--surface);
            border-right: 1px solid var(--border);
            display: grid;
            grid-template-rows: auto auto 1fr;
            overflow: hidden;
            min-height: 0;
        }"""

# 2. Base .note-list
old_base_notelist = """        .note-list {
            flex: 1 1 0;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            min-height: 0;
            padding: 8px;
        }"""
new_base_notelist = """        .note-list {
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            min-height: 0;
            padding: 8px;
        }"""

# 3. Mobile .sidebar
old_mobile_sidebar = """      .sidebar { width: 100%; height: 100%; overflow: hidden; border-right: none; display: flex; flex-direction: column; }"""
new_mobile_sidebar = """      .sidebar { width: 100%; height: 100%; overflow: hidden; border-right: none; display: grid; grid-template-rows: auto auto auto 1fr; }"""

# 4. Mobile .note-list
old_mobile_notelist = """      .note-list {
        flex: 1 1 0;
        min-height: 0;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
      }"""
new_mobile_notelist = """      .note-list {
        min-height: 0;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
      }"""

content = content.replace(old_base_sidebar, new_base_sidebar)
content = content.replace(old_base_notelist, new_base_notelist)
content = content.replace(old_mobile_sidebar, new_mobile_sidebar)
content = content.replace(old_mobile_notelist, new_mobile_notelist)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Grid layout replacement applied.")
