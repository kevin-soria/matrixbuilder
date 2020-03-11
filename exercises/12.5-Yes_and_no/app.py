theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def seperations(boolens):
    new_list = []
    if boolens == 1:
        new_list.append(str('wiki'))
    else:
        new_list.append(str('woko'))
    return(new_list)


results = list((map(seperations, theBools)))
print(results)

