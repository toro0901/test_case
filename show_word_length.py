def show_word_length(words_list):
    for word in words_list:
        print(f"{word}:{len(word)}")


words = ["apple", "banana", "cherry"]
show_word_length(words)