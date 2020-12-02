import sys, os, math
def find_match():
    name = input('\nWhats your name?\n')
    smallest = 0
    file = open((name + '.txt'), 'r')
    my_content = file.read()
    my_info = []
    your_info = []
    smallest_info = []
    cache = ''
    for i in my_content:
        if i == ' ':
            my_info.append(cache)
            cache = ''
        else:
            cache += i
    for f in os.listdir():
        cache = ''
        if f.endswith(".txt") and f != name + '.txt':
            file = open(f, "r")
            content = file.read()
            for y in content:
                if y == ' ':
                    your_info.append(cache)
                    cache = ''
                else:
                    cache += y
            score = (compare(my_info, your_info))
            if score > smallest:
                smallest = score
                smallest_info = your_info[:4]
            your_info = []
    if smallest_info == []:
        print('No match!\n')
    else:
        print(smallest, smallest_info, '\n')
def compare(me, you):
    if me[1] != you[3] or you[1] != me[3]:
            return 0
    elif not (int(me[2]) - 5 < int(you[2]) < int(me[2]) + 5):
        return 0
    answers_me = me[(me.index('$'))+1:]
    answers_you = you[(you.index('$'))+1:]
    count = 0
    for i in range(len(answers_me)-1):
        if int(answers_me[i]) - 1 <= int(answers_you[i]) <= int(answers_me[i]) + 1:
            count += 1
    return(round(count / len(answers_me),3) * 100)
            
