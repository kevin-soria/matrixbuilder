all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
color = []
for x in all_colors:
    if x["sexy"] == True:
        color.append(x["label"])
        
    
# print(color)

def print_ul(elements):
    print("<ul>")
    for s in elements:
        ul = "<li>" + str(s) + "</li>"
        print(ul)
    print("</ul>")
print_ul(color)

