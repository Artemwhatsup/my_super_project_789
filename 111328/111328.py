f = open("input.txt", "rt")
print(f.read())
f.close()

with open('input.txt', 'r') as f:
    reverse_string = f.readline()[::-1]
    print(reverse_string)