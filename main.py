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
        
    return int(coll["*"])
    
def posWords():
    o = t = r = f = i = list(string.ascii_uppercase)
    print(i)
    count = asstCount()
    arrs = [o,t,r,f,i][0:count]
    for y in range(len(arrs)):

        for x in range(26):
            arrs
            for z in range(26):


        
posWords()
