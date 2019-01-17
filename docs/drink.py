def satisfied_cust(d,ls):
    """
    remove all the satisfied customers from the values of other drinks
    return updated dict
    """
    for drinks in d:
        if len(d.get(drinks)):
            continue
        for cust in ls:
            if cust in d[drinks]:
                d[drinks].remove(cust)
    return d

def find_most_fev_drink(d):
    """
    get the drink which is commonly asked in most customers
    serve that drink(remove it from dict)
    return satisfied customers list and updated dict
    """
    fev_cust_count = -1
    ls = []
    val = -9
    for drinks in d:
        if not(d.get(drinks)):
            continue
        
        if fev_cust_count < len(d[drinks]):
            fev_cust_count = len(d[drinks])
            ls = d[drinks]
            val = drinks
    d.pop(val)
    return ls, d

def create_drinks_dict(m,d_list):
    """
    Swap values with keys and regenerate the dict
    keys: drinks
    values: customers
    return the new dict
    """
    d = dict()
    for drink in d_list:
        for cust in m:
            if drink in m[cust]:
                try:
                    d[drink].append(cust)
                except KeyError:
                    d[drink] = [cust]
    return d


# get the inputs
n = input()
d = input()

m = dict()

# store the prefered drinks in the dict according to customers
for i in range(1,n+1):
    m[i] = map (int , raw_input().split())

cust_list = m.keys()

# get expected dict
dd = create_drinks_dict(m, cust_list)

# counter for number of servings
count = 0
while True:
    # wait till all customers get satisfied
    if not cust_list:
        break
    
    count+=1
    # get list of customers and updated dict with most common desire
    ll,dd = find_most_fev_drink(dd)

    # remove satisfied customers from the dict
    dd = satisfied_cust(dd,ll)
    
    # remove satisfied customers from the list
    for cust in ll:
        if cust in cust_list:
            cust_list.remove(cust)

            
print count
