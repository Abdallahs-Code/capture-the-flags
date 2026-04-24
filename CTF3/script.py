with open("shifted.txt", "r") as f:
    numbers = list(map(int, f.read().split()))

flag = ''.join(chr(n >> 1) for n in numbers)
print(flag)