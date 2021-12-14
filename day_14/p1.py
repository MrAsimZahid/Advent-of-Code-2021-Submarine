from  collections import Counter

# input
data = [each.strip() for each in open('input.txt', 'r')]

# print(data)

polymer_template = data.pop(0)
data.pop(0)

# print(data)


def get_pairs(data):
    pair_dict = {}
    for each in data:
        pair, element = each.strip().split(' -> ')
        pair_dict[pair] = element
    return pair_dict



pairs = get_pairs(data)
# print(type(pairs))
# print(pairs)

# polymer_template = "NNCB"

for count in range(40):
    print(count)
    append_element = []
    for each in range(len(polymer_template)):
        if each == len(polymer_template) -1:
            append_element.append(polymer_template[each])
            break
        first, second = polymer_template[each], polymer_template[each+1]
        # print(first, second)
        key = first+second
        element = pairs[key]
        append_element.append(first)
        append_element.append(element)
        # append_element.append(second)
    polymer_template = ''.join(append_element)
    # print(polymer_template)

# append_element.most_common()
most = Counter(append_element).most_common()[0]
least = Counter(append_element).most_common()[-1]
# print(most)
# print(least)
print(most[1] - least[1])
print(len(polymer_template))