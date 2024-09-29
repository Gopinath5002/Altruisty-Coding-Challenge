def qsn1(n,prices):
    maxi_prof=0
    mini_price=float('inf')
    for i in range(n):
        mini_price=min(mini_price,prices[i])
        profit=prices[i]-mini_price
        maxi_prof=max(profit,maxi_prof)
    return maxi_prof
print(qsn1(6,[7, 1, 5, 3, 6, 4]))
