def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for c in text.lower():
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

