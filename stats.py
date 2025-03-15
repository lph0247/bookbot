def get_num_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_set = set(text.lower())
    result = {}
    for char in char_set:
        result[char] = text.lower().count(char)
    return result

def sort_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char":ch, "num":dict[ch]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]