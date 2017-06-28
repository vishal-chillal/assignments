# 45.A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

# Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.


def get_name_list(file_name):
    fp = open(file_name,"r")
    #    ls = fp.read().split("#")[0].split()
    ls = fp.read().replace("#","\n").split()
    fp.close()
    print ls,"\n\n"
    return ls

def create_char_dict(name_list):
    char_dict = {}
    for name in name_list:
        if name[-1] not in char_dict:
            char_dict[name[-1]] = [{},{name}]
        elif char_dict[name[-1]][1] == {} :
            char_dict[name[-1]][1] = {name}
        else:
            char_dict[name[-1]][1].add(name)


        if name[0] not in char_dict:
            char_dict[name[0]] = [{name},{}]
        elif char_dict[name[-1]][0] == {}:
            char_dict[name[0]][0] = {name}
        else:
            char_dict[name[-1]][0].add(name)

    return char_dict

def get_chain(name,char_dict,name_list, sequence):
    if char_dict[name[-1]][0] != {}:
        chain_list = []
        for new in char_dict[name[-1]][0]:
            if new in sequence:
                continue
            chain_list.append( get_chain(new,char_dict,name_list,sequence.append(new)))
        if chain_list == []:
            return []
        return max(chain_list, key = len)
    return sequence

        
    

def longest_name_chain():
    name_list = get_name_list("pokemon_name_list.txt")
    char_dict = create_char_dict(name_list)
    my_dict = {}
    for i in name_list:
        my_dict[i] = get_chain(i,char_dict,name_list,sequence = [i])
    return my_dict

d = longest_name_chain()
for i in d.items():
    print i

print "\n\n",max(d.values(), key = len)
