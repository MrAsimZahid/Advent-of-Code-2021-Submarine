"""
Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

# find most common bit values 
# find least commmon bit values
# multiply 


gamma_rate = 0  
epsilon_rate = 0
data = [each.strip() for each in open('binary_input.txt', 'r')]
zero = 0
one = 0

common_data = ""

for i in range(len(data[0])):
    print(i)
    zero = 0
    one = 0
    
    for each in range(len(data)):
        bit = data[each][i]
        print(type(bit))
        if bit == '0':
            zero += 1
        elif bit == '1':
            one += 1
    if zero > one:
        common_data += '0'
    elif one > zero:
        common_data += '1'
print(common_data)


gamma_rate = int(common_data, 2)
rev_common_data = ""
for each in common_data:
    if each == '0':
        rev_common_data += '1'
    elif each == '1':
        rev_common_data += '0'
print(rev_common_data)
epsilon_rate = int(rev_common_data, 2)


print(gamma_rate * epsilon_rate)