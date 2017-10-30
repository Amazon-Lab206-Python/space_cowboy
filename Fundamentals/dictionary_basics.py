myinfo = {
    'name': 'Brad Guh-iles',
    'location': 'Sydney, Australia',
    'hobbies': 'Surfing, Coding, Playing Guitar, Writing, Being Awesome in General'
}

myinfo['name'] = 'Sam Ferrante'

# # x = [('name', 'Felix'), ('location', 'Seattle')]
# # for key,val in x: # for whatever in a list
# #     print key, val

# #basic, always works-level
# for key in myinfo:
#     print key, myinfo[key]

# #advanced
for key, val in myinfo.items():
    print key, val