from .counter import words_counter , line_counter , character_counter

def main():
    path = input("please input the path of text file:  ")
    while True:
        try:

            words_list , words_count = words_counter(path)
            line_count = line_counter(path)
            character_count = character_counter(path)
            longest_word = max(words_list, key=len, default="")
            break

        except FileNotFoundError:
            print("file not exist")
            path = input("please input the path of text file:")

    return f"the longest word: {longest_word}\nwords count: {words_count}\nnon empty lines count: {line_count}\nused characters count: {character_count}"




if __name__ == "__main__":
    print(main())
