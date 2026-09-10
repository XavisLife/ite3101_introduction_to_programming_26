def censor(text: str, word: str) -> str:
    """
    Censors a specific word in the given text by replacing it with asterisks.

    Args:
        text (str): The input text to be censored.
        word (str): The word to be censored.

    Returns:
        str: The censored text with the specified word replaced by asterisks.
    """
    # Create a string of asterisks with the same length as the word to be censored
    censor_word = '*' * len(word)

    # Replace all occurrences of the word in the text with the censor_word
    censored_text = text.replace(word, censor_word)

    return censored_text
