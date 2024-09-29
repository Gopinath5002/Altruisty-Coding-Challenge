def qsn2(s,st_idx,end_idx):
    combined=zip(st_idx,end_idx)
    arr=[]
    for (i,j) in combined:
        post=False
        ans=0
        temp=0
        for k in s[i-1:j]:
            if k=='|':
                ans+=temp
                temp=0
                post=True
            if post and k=='*':
                temp+=1
        arr.append(ans)
    return arr
print(qsn2('|**|*|',[1,1],[5,6]))
