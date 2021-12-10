# input
data = [each.strip() for each in open('stack_input.txt', 'r')]


points = 0
for each in data:
    inlist = ['{', '[', '<','(']
    outlist = ['}', ']', '>', ')']
    check_dict = {'}':'{', ']':'[', '>':'<', ')':'('}
    stack = []
    for i in each:
        if i in inlist:
            stack.append(i)
        elif i in outlist:
            if len(stack) == 0:
                print('False')
                break
            elif check_dict[i] != stack.pop():
                if i is ')':
                    points += 3
                if i is '}':
                    points += 1197
                if i is ']':
                    points += 57
                if i is '>':
                    points += 25137
                break


print(points)

