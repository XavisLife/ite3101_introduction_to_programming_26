def reverse(text):
    reversed_text = ""
    for i in range(Len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text
