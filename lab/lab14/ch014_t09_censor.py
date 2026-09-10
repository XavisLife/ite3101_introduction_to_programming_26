def censor(text: str, word: str) -> str:
    words = text.split(" ")
    asterisks = "*" * len(word)

    for i in range(len(words)):
        if words[i] == word:
            words[i] = asterisks

    return " ".join(words)
