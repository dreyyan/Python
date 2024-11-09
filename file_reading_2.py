with open('.txt/test.txt', 'r') as f:
    size_to_read = 20
    read_content = f.read(size_to_read)
    print(read_content, end='')
    f.seek(0) # Redirects back to first character
# f.close() # No need to f.close() when using 'with'