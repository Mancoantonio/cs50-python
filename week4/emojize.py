import emoji

def main():
    word = input("Input: ")
    output = emoji.emojize(word, language='alias')
    print(output)

main()