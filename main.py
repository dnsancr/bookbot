with open('books/frankenstein.txt') as f:
    file_content = f.read()
    f.close()
    #print(file_contents)
    words = file_content.split()
    print(len(words))
