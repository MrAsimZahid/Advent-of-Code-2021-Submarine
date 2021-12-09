
data = [[int(i) for i in each.split(",")] for each in open('compound_fule_input.txt', 'r')][0]

# data = [16,1,2,0,4,2,7,1,2,14]

def loss(value):
    loss_sum = []
    for each in data:
        diff_val = abs(each - value)
        # first, last = (value*(value+1))/2, (diff_val*(diff_val+1))/2
        loss_sum.append((diff_val*(diff_val+1))/2)
    return sum(loss_sum)

min_d, max_d = min(data), max(data)


sum_d = []
for each in range(min_d, max_d):
    sum_d.append(loss(each))

print(min(sum_d))
