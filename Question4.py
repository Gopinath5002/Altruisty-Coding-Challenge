from collections import Counter
def qsn4(n,b):
    b=list(map(lambda x : x.lower(),b))
    count=Counter(b)
    for i in count:
        if count[i]%2:
            return i
    return 'All Are Even'
print(qsn4(10,['a','b','b','b','c','c','c','a','f','c'] ))
