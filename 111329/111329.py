f = open("words.txt", "rt")
print(f.readlines())
f.close()

with open('words.txt', 'r') as f:
    reverse_string = f.readlines()[::-1]
    for line in reverse_string:
        pass
    print(reverse_string)