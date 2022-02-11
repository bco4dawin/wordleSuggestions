import collections, string, itertools
def getWord():
    letters = input("Enter your letters(* for spaces)").upper()

    if len(letters) > 5:
        print("Word was too long, try again")
        getWord()
    else:
        return letters
        
def asstCount():
    word = getWord()
    
    coll = collections.defaultdict(int)
    for c in word:
        coll[c] += 1
        
    return coll["*"]
    
def posWords():
    o=t=r=f=i = list(string.ascii_uppercase)
    arrs = [o,t,r,f,i]
    count = asstCount()
    for i in range(count):
        word = itertools.permutations([arrs[0:count]])
        word = "".join(word)
        print(word)
        
posWords()
        
