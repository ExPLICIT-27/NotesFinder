import os

def remove_null_bytes(file_path):
    """Read a file and remove any null bytes, then write it back."""
    try:
        # Read the file content
        with open(file_path, 'rb') as file:
            content = file.read()
        
        # Remove null bytes
        cleaned_content = content.replace(b'\x00', b'')
        
        # Write back the cleaned content
        with open(file_path, 'wb') as file:
            file.write(cleaned_content)
        
        print(f"Processed {file_path}: Removed {len(content) - len(cleaned_content)} null bytes")
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Files to clean
files_to_clean = [
    'books/management/commands/import_csv.py',
    'books/management/commands/__init__.py',
    'books/management/__init__.py'
]

# Process each file
for file_path in files_to_clean:
    if os.path.exists(file_path):
        remove_null_bytes(file_path)
    else:
        print(f"File not found: {file_path}")

print("\nDone! Try running your Django command again.") 