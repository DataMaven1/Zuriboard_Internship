# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, 'r') as f:
        file = f.read()
        return (file)


def count_words(str):
    dict_words = {}
    str_01 = list(str.split())

    for i in str_01:
        dict_words.update({i: str_01.count(i)})
    
    print(dict_words)

text = read_file_content("story.txt")
count_words(text)
    
