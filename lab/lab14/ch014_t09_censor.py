def censor(text: str, word: str) -> str:
    censor = "*" * len(word)
    return text.replace(word, censor)
