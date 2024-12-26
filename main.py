def wc(str):
    count = 0
    for word in str:
        count += 1
    return count

def charcounter(str):
    chardict = {}
    for char in str:
        if char.isalpha():
            chardict[char.lower()] = chardict.get(char.lower(),0) + 1
    return chardict


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    
        word_count = wc(file_contents)
        char_count = charcounter(file_contents)
        print(word_count)
        
        list_dicts = []
        for key,value in sorted(char_count.items(),reverse=True,key=lambda item:item[1]):
            print(key,value)
        
main()
