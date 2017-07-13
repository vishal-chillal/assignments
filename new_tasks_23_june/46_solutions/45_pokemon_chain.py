# 45.A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

# Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.


def get_name_list(file_name):
    fp = open(file_name,"r")
    ls = fp.read().split()
    fp.close()
    return ls

def create_char_dict(name_list):
    char_dict = {}
    for name in name_list:
        try:
            char_dict[name[0]].add(name)
        except:
            char_dict[name[0]] = {name}

    return char_dict

def select_name_from_set(name_set):
    k = list(name_set)
    k.sort()
    op = filter(lambda x:x[0] == x[-1],k)
    try:
        name = op[0]
    except IndexError:
        name = k[len(k)/2]
    return name

def generate_dict(name, char_dict):
    ls = []
    if name[-1] in char_dict and char_dict[name[-1]] != set([]):
        while char_dict[name[-1]] != set([]):
            i = select_name_from_set(char_dict[name[-1]])
            char_dict[name[-1]].remove(i)
            new = generate_dict(i,char_dict)
            if len(new) > len(ls):
                ls = new
                if ls != []:
                    char_dict[ls[0][0]].add(ls[0])
    return [name]+ls

def get_chain(char_dict, name_list):
    ls = []
    
    for i in name_list :
        tmp_dict = create_char_dict(name_list)
        new = generate_dict(i,tmp_dict)
        if len(ls) < len(new):
            ls = new

    print "\nlen",len(ls),"\n\n",ls

if __name__ == "__main__":
    name_list = get_name_list("pokemon_name_list.txt")
    char_dict = create_char_dict(name_list)
    for i in char_dict.items():
        print i[0], "\t", i[1]
    get_chain(char_dict, name_list) 

