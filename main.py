def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        wordcount = 0
        words = file_contents.split()

        character_count = {}

        for word in words:
            wordcount += 1
            for char in word:
                character_count[char.lower()] += 1

        print(wordcount)
        print(character_count)


        
main()
