import re

with open("input.txt") as f:
    data = f.read().strip()


def calibration(data):
    ls = data.split("\n")
    # first we find all the numbers in the string
    ns = [re.findall("\d", x) for x in ls]
    # then sum the first and the last number of each string (each line)
    return sum(int(n[0] + n[-1]) for n in ns)


# Part 1
print(calibration(data))

# Part 2
data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)
print(calibration(data))
