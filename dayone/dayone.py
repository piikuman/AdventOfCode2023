file = open('input.txt', 'r')


# Part 1
sum = 0
for line in file:
    line = line.strip()
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    sum += int(digits[0] + digits[-1])
print("Part 1 sol: ", sum)
