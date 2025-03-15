with open('.txt/test.txt', 'r') as f:
    readContent = f.read()
    print(readContent)
print(f'Mode: {f.mode}')

# Basic
# f = open('.txt/test.txt', 'r')
# readContent = f.read()
# print(readContent)
# print(f'Mode: {f.mode}')
# f.close()

# Larger Contents
# with open('.txt/test.txt', 'r') as f:
    # for line in f:
        # print(line, end='')
    # f.close()
