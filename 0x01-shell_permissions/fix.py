import os

def fix_line_endings_in_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        # Replace CRLF with LF
        fixed_content = content.replace(b'\r\n', b'\n')
        with open(file_path, 'wb') as f:
            f.write(fixed_content)
        print(f"✅ Fixed: {file_path}")
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")

# Walk through all files in current directory
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        # Only fix text files
        if 'text' in os.popen(f'file "{file_path}"').read():
            fix_line_endings_in_file(file_path)
