
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']


#Your code go here:
# def am_func(example):
#     newex = []
#     for n in names:
#         if "am" in n:
#             newex.append(n)
#     return(newex)

# resulting_names = list(am_func(names))

# print(resulting_names)

print([x for x in names if "am" in x.lower()])