def pangram(phrase):
    letter={"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    phr=set(phrase)
    if phr>=letter:
        return True
    else:
        return False
print(pangram("the quick brown fox jumps over the lazy dog"))