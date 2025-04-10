def word_count(text):

    words = text.split()
    count = 0

    for word in words:
        count += 1

    return count

def char_count(text):
    text = text.lower()
    chars = set(text)
    ch_count = {}

    for char in chars:
        if char.isalpha():
            count = 0
            for i in range(0, len(text)):
                if char == text[i]:
                    count += 1
            ch_count[char] = count

    return ch_count

def sort_on(dict):
    return dict[1]

def to_sort(ch_count):
    ch_list = list(ch_count.items())
    ch_list = sorted(ch_list,key=sort_on,reverse=True) 
    return ch_list