def censor(text: str, word: str) -> str:
    words = text.split()
    censor = "*" * len(word)

    for i in range(len(words)):
        if words[i] == word:
            words[i] = censor

    return " ".join(words)
