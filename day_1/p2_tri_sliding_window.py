num_increase = 0
previous_sum = 0
data = [int(each.strip()) for each in open('input.txt', 'r')]

for i in range(len(data)):
    if data[i]+data[i-1]+data[i-2] > data[i-1]+data[i-2]+data[i-3]:
        num_increase += 1
    # sliding window approach
    # current_sum = sum(data[i:i+3])
    # if current_sum > previous_sum:
    #     num_increase += 1
    # previous_sum = current_sum

print(num_increase) 