def solution(n):
    # handled the base condition here
    if n==1:
	print("*")
        return
    star_patern = '*'
    hash_patern = '#'
    half = n / 2
    s = ""
    # run the loop for half the size and print common patern
    for x in range(1, half + 1):
        if x % 2:
            print(star_patern * x) + (hash_patern * (n - x))
        else:
            print(hash_patern * (n - x)) + (star_patern * x)

    if (n % 2):
        # if input is Odd, handle two flows
        if half % 2:
            print(hash_patern * (n - half-1)) + (star_patern *( half+1))
            for x in range(half, 0, -1):
                if not x % 2:
                    print(hash_patern * (n - x)) + (star_patern * x)     
                else:
                    print(star_patern * x) + (hash_patern * (n - x))
        else:
            print(star_patern * (half + 1)) + (hash_patern * (n - half-1))
            for x in range(half, 0, -1):
                if not x % 2:
                    print(hash_patern * (n - x)) + (star_patern * x)                
                else:
                    print(star_patern * x) + (hash_patern * (n - x))

    else:
        # handle if input is even 
        for x in range(half, 0, -1):
            if not x % 2:
                print(star_patern * x) + (hash_patern * (n - x))
            else:
                print(hash_patern * (n - x)) + (star_patern * x)

n = input()
solution(n)
