import os
import codecs

def convert_encoding(root_dir, from_enc="shift_jis", to_enc="utf-8"):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with codecs.open(filepath, 'r', from_enc) as file:
                    content = file.read()
                with codecs.open(filepath, 'w', to_enc) as file:
                    file.write(content)
            except UnicodeDecodeError:
                print(f"Decode error at {filepath}, might not be a text file or might be in another encoding.")
            except Exception as e:
                print(f"Failed to convert {filepath}: {e}")

convert_encoding('.')
