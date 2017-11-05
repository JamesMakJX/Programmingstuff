#fail
def check(string):
    dist = []
    for ii in range(len(string)):
        for i in range(len(string)-ii-1):
            if string[ii] == string[1+i+ii]:
                dist.append(i+1)

    if dist == []:
        return 'none'
    print(dist)
    print(string[dist.index(min(dist))])
            
