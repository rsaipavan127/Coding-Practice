def sortbylen(string):
    string.sort(key=lambda x:len(x), reverse=True)
    print(string)
    




l=["abc","kim","titanic","september","july"]
sortbylen(l)