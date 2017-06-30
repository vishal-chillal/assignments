# 45.A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

# Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.


def get_name_list(file_name):
    fp = open(file_name,"r")
    ls = fp.read().replace("#","\n").split()
    fp.close()
    return ls

def create_char_dict(name_list):
    char_dict = {}
    for name in name_list:
        if name[0] not in char_dict:
            char_dict[name[0]] = {name}
        else:
            char_dict[name[0]].add(name)

    return char_dict


def generate_dict(name, char_dict):
    if name[-1] not in char_dict or char_dict[name[-1]] == set([]):
        return [name]
    else:
        if name  in char_dict[name[0]]:
            char_dict[name[0]].remove(name)
        ll = char_dict[name[-1]]
        ls = []
        while char_dict[name[-1]] != set([]):
            i = char_dict[name[-1]].pop()
            ls.append(generate_dict(i,char_dict))
        return [name]+max(ls,key = len)


def get_chain(char_dict, name_list):
    ls = []
    
    for i in name_list :
        tmp_dict = create_char_dict(name_list)
        ls.append(generate_dict(i,tmp_dict))

    ans = max(ls,key = len)
    print "len",len(ans),"\n\n",ans


def longest_name_chain():
    name_list = get_name_list("pokemon_name_list.txt")
    char_dict = create_char_dict(name_list)
    get_chain(char_dict, name_list) 

longest_name_chain()
