def last_word_length(s):
    return len(s.strip().split(" ")[-1])

sentence = "This is an apple"
print("The length of the last word is:", last_word_length(sentence))
