def censor(text: str, word: str) -> str:
    for character in word:
        if character in text:
            text = text.replace(character, "*")
            