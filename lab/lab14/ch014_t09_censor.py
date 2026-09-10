def censor(text: str, word: str) -> str:
    for i in range(len(word)):
        if character in text:
            text = text.replace(character, "*")
    return text
