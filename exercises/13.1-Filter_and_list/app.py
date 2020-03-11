
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def only_rs(oldlist):
    return(oldlist[0] == 'R')
 
resulting_names = list(filter(only_rs, list(all_names)))

print(resulting_names)
# ----------------------------------------
# 1
# >>> list = ["abcd", "defg", "abc", "defg", ".", "a"]
# 2
# >>> reslst = filter(lambda x: x[0] == 'a', list)
# 3
# >>> reslst
# 4
# ['abcd', 'abc', 'a']
# 5
# >>>




