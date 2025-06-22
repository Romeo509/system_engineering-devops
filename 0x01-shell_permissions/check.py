file_path = "0-iam_betty"  # Change this to your script's filename

with open(file_path, "rb") as f:  # Read in binary to catch \r
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    decoded = line.decode("utf-8", errors="replace")
    print(f"Line {i}: {repr(decoded.strip())} → {len(decoded.strip())} characters (raw length: {len(decoded)})")
