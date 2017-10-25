word_list = ['hello','world','my','name','is','Anna']
char = 'o'

for val in word_list:
    if (val.find(char)!=-1):
        print val



#provided solution
def find_character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):

        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])

    print new_list

test_list = ['hello','world','my','name','is','Anna']
find_character(test_list, 'o')