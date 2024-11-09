with open(".txt/test.txt", 'r') as original_file:
    with open(".txt/copy_test", 'w') as new_file:
        for line in original_file:
            new_file.write(line)