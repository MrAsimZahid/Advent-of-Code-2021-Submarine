num_increase = 0
previous = None
for each in open('input.txt', 'r'):
    each = int(each.strip())
    if previous is not None and each > previous:
        num_increase += 1
    previous = each
print(num_increase) 