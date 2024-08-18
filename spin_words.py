def spin_words(sentence):
    array_sentence = sentence.split()
    for i, word in enumerate(array_sentence):
        if len(word) > 4:
            array_sentence[i] = word[::-1]
    return " ".join(array_sentence)


print(spin_words("Hey wollef sroirraw"))
