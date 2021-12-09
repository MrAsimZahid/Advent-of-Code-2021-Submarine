
# data = [int(each.strip()) for each in open('crab_input.txt', 'r')]

data = [[int(i) for i in each.split(",")] for each in open('crab_input.txt', 'r')]

# data = [16,1,2,0,4,2,7,1,2,14]

def loss(value):
    loss_sum = []
    for each in data:
        loss_sum.append(abs(each - value))
    return sum(loss_sum)

min_d, max_d = min(data), max(data)


sum_d = []
for each in range(min_d, max_d):
    sum_d.append(loss(each))

print(min(sum_d))
