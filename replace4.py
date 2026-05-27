import sys

filename = r"c:\Users\uppro\Sync\O_Mar_26\ClaudeCode_CoWork_OS\SuperNotes_26\SuperNotes.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

target = """      .note-list {
        flex: 1;
        height: auto;
        min-height: 0;
        overflow-y: scroll !important;
        -webkit-overflow-scrolling: touch;
      }"""
repl = """      .note-list {
        flex: 1 1 0%;
        height: 0;
        min-height: 0;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior: contain;
      }"""

if target in content:
    content = content.replace(target, repl)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacement successful.")
else:
    print("Target not found. Let's do a regex replacement just in case of spaces.")
    import re
    # Match the block even if spacing is slightly different
    pattern = re.compile(r'\.note-list\s*\{\s*flex:\s*1;\s*height:\s*auto;\s*min-height:\s*0;\s*overflow-y:\s*scroll\s*!important;\s*-webkit-overflow-scrolling:\s*touch;\s*\}')
    if pattern.search(content):
        content = pattern.sub(repl, content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Regex replacement successful.")
    else:
        print("Regex target not found.")
