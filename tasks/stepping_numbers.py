import sys
input = map(int, sys.argv[1].split(','))

def get_stepping_numbers(N):
    ls = []
    if N == 2:
        ls = [10]
    end = eval(str(1)+("0")*N)
    start = int("".join([str(x) for x in range(1,N+1)]))
    second = "".join([str(x) for x in range(N,0,-1)])
    reversed(second)
    second = int(second)
    print second
    while len(str(second)) < N+1:
        if int(start) % 10:
            ls.append(start)
        ls.append(second)
        start += int("1"*N)
        second += int("1"*N)
    return sorted(ls)

for i in input:
    op =  get_stepping_numbers(i)
    print len(op) , op
    
