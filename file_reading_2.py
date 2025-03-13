with open('.txt/test.txt', 'r') as f:
    size_to_read = 20
    read_content = f.read(size_to_read)
    print(read_content, end='') # End with blank instead of newline
    f.seek(0) # Redirects back to first character
