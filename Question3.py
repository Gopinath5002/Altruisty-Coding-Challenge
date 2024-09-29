def qsn3(k,n,space):
    maxi=0
    for i in range(n-k+1):
        maxi=max(maxi,sum(space[i:i+k]))
    return maxi
print(qsn3(3,8,[1,2,3,2,1,1,9]))
