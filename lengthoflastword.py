def lengthOfLastWord(s) :
    return len(s.rstrip().split(" ")[-1])

s = "hehe haha"
print(lengthOfLastWord(s))  
