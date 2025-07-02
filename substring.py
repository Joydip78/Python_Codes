def lengthOfLongestSubstring(s):
    sCopy = ""
    print("length : ")
    c = 0
    if s != "":
        cC = 0
        for i in s:
            x = inS(s, i)
            print(x)
            if x != 0:
                sCopy = i
                cC = 1
            else:
                sCopy += i
                cC += 1
            c =max(c,cC)
    return c
def inS(s, i):
     c = 0
     for j in s:
          if i == j:
               return c
          else:
               c += 1
     return 0

s = "abcae"
print(lengthOfLongestSubstring(s))
s = "bbbbbbb"
print(lengthOfLongestSubstring(s))
s = ""
print(lengthOfLongestSubstring(s))
s = "dvdf"
print(lengthOfLongestSubstring(s))