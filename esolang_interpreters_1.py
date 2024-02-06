def my_first_interpreter(code):
    resposta = ""
    number = 0
    for letter in code:
        if number > 255:
            number = 0

        if letter == "+":
            number += 1
        if letter == ".":
            resposta = resposta + chr(number)

    return resposta
