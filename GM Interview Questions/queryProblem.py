import sys

board = [[0 for j in range(256)] for i in range(256)] # Create 256x256 matrix

def set_row(i, x):
    for j in range(256):
        board[i][j] = x

def set_col(j, x):
    for i in range(256):
        board[i][j] = x

def query_row(i):
    return sum(board[i])

def query_col(j):
    return sum(board[i][j] for i in range(256))


for line in sys.stdin:
    print(line, end="")
    while True:
        try:
            line = line.strip().split()

            if line[0] == "SetRow":
                set_row(int(line[1]), int(line[2]))

            elif line[0] == "SetCol":
                set_col(int(line[1]), int(line[2]))

            elif line[0] == "QueryRow":
                print(query_row(int(line[1])))

            elif line[0] == "QueryCol":
                print(query_col(int(line[1])))
           
        except EOFError:
            break
       

    
