line = "86,2,3"

def bitPositions(n, p1, p2):
    return (n & (1 << (p1 -1))) == (n & (1 << (p2-1)))

n, p1, p2 = [int(x) for x in line.strip().split(',')]
result = (n & (1 << (p1 - 1))) == (n & (1 << (p2 - 1)))
print("true" if result else "false")