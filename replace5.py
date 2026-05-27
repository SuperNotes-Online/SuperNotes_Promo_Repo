import sys
import re

filename = r"c:\Users\uppro\Sync\O_Mar_26\ClaudeCode_CoWork_OS\SuperNotes_26\SuperNotes.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix base CSS
base_target = """        .note-list {
            flex: 1;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            overscroll-behavior: contain;
            min-height: 0;
            padding: 8px;
            height: 0;
        }"""
base_repl = """        .note-list {
            flex: 1 1 0;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch;
            min-height: 0;
            padding: 8px;
        }"""

# Fix mobile CSS
mobile_target = """      .note-list {
        flex: 1 1 0%;
        height: 0;
        min-height: 0;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior: contain;
      }"""
mobile_repl = """      .note-list {
        flex: 1 1 0;
        min-height: 0;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
      }"""

content = content.replace(base_target, base_repl)
content = content.replace(mobile_target, mobile_repl)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced both blocks successfully.")
