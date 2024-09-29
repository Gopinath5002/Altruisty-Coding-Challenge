def qsn5(oxy_lvl):
    dic={}
    maxi=0
    for i in range(3):
        val=(oxy_lvl[i]+oxy_lvl[i+3]+oxy_lvl[i+6])//3
        maxi=max(maxi,val)
        dic[i]=val
    arr=[str(i+1) for i in dic if dic[i]==maxi]
    s=''
    for i in arr:
        s+=f'Trainee Number :{i}\n'
    return s
print(qsn5([95,90,92,92,90,95,90,90,90]))
