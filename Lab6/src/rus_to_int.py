def rus_to_int(char: str):
    char_lower = char.lower()

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    for ch in alphabet:
        if char_lower == ch:
            return alphabet.index(ch)
    
    raise ValueError(f"{ch} - не русская буква")
