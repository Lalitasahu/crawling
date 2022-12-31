n = 1
def mystery(n):
    v = 0
    for i in range(1,n+1):
        sum = ''
        for j in range(1,i+1):
            sum+= str(i)
        v+=int(sum) 
    return(v)

print(mystery(1))
print(mystery(2))
print(mystery(3))
print(mystery(4))


