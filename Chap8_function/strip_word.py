# WAP to strip the given words using function 
def strip_word(l, word):
    n = []
    for items in l:
        if not(items ==  word):
            n.append(items.strip(word))
        return n
    l = ["HelloWorld", "WorldPeace", "PeaceWorld"]
    print(strip_word(l, "World"))
      