def train(n):
    a = [[] for i in range(n)]
    for i,j in enumerate(a):
        if i == 0:
            j.append(1)
        elif i == 1:
            j.extend([1,1])
        else:
            for f in range(i):
                if f == 0:
                    j.append(1)
                try:
                    j.append(a[i-1][f] + a[i-1][f+1] )
                except:
                    print(f)
                    j.append(a[i-1][f])


    return a


    
print(train(7))
