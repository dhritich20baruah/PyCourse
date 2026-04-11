import hashlib

extracted = []

try:
    with open ("server_logs.txt", 'r') as file:
        for line in file:
            if line.startswith("SERVER") or line.startswith("-") or line == "\n":
                continue

            line_hash = hashlib.md5(line.encode('utf-8')).hexdigest()

            last_char = line_hash[-1]

            if last_char.isdigit():
                char_at_4 = line[4]
                extracted.append(char_at_4)
                print(f"KEEP | Hash: {line_hash} | Index 4: '{char_at_4}'")
            else:
                # DISCARD the line (ends in a-f)
                continue

except FileNotFoundError:
    print("file not found")