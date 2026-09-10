def anti_vowel(text):
    vowels = "aeiou"
    for character in text:
        if character.lower() in vowels:
            text = text.replace(character, "")
    return text
