def disemvowel(string_):
    array = [letra for letra in string_]
    array_correto = [word for word in array if word.lower() not in "aeiou"]
    return "".join(array_correto)


print(disemvowel("ola voce esta muito bela nesto noite de hoje"))
