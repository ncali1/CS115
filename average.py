with open(r'numbers.txt') as f:
    data = [float(line.rstrip()) for line in f]
print(sum(data)/len(data))
