def count_word(word, text):
    symbols = {}
    lower_text = text.lower()
    lower_word = word.lower()
    
    if len(text) < len(word):
        return 0
    
    if lower_word == lower_text:
        return 1
    
    uniq_word_symbols = set([*lower_word])

    for ch in uniq_word_symbols:
        ch_count = lower_word.count(ch)
        ch_count_text = lower_text.count(ch)

        symbols[ch] = ch_count_text // ch_count

    min_symbols_count = min(symbols, key=lambda x: symbols[x])
    print(symbols)
    return symbols[min_symbols_count]


def count_word_test():
    words = [
        "Rumpelstilskin",
        "tale",
        "mage",
        "bitter"
    ]

    text = "Rabbits under moonlight play, elves laugh, singnig tales in late summer, kittens in nest."

    for word in words:
        res = count_word(word=word, text=text)
        print(f"Word {word} can be constructed {res} times")
