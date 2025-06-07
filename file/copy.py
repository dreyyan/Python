def copyFile(oldFilename, newFilename) -> None:
    with open(oldFilename, 'r') as oldFile:
        with open(newFilename, 'w+') as newFile:
            for line in oldFile:
                newFile.write(line)

            newFile.seek(0) # reset pointer
            content = newFile.read()
            print(content)
 
copyFile("code/Python/file/test.txt", "code/Python/file/newTest.txt")
