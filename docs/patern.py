n = input()
p1 = '*'
p2 = '#'
v = n / 2
if n==1:
	print("*")
else:
	for x in xrange(1, v + 1):
	    if x % 2:
		print(p1 * x) + (p2 * (n - x))
	    else:
		print(p2 * (n - x)) + (p1 * x)

	if (n % 2):
	    if v % 2:
		print(p2 * (n - v-1)) + (p1 *( v+1))
		for x in xrange(v, 0, -1):
		    if not x % 2:
		        print(p2 * (n - x)) + (p1 * x)     
		    else:
		        print(p1 * x) + (p2 * (n - x))

		        

	    else:
		print(p1 * (v + 1)) + (p2 * (n - v-1))
		for x in xrange(v, 0, -1):
		    if not x % 2:
		        print(p2 * (n - x)) + (p1 * x)                
		    else:
		        print(p1 * x) + (p2 * (n - x))



	else:
	    for x in xrange(v, 0, -1):
		if not x % 2:
		    print(p1 * x) + (p2 * (n - x))
		else:
		    print(p2 * (n - x)) + (p1 * x)
