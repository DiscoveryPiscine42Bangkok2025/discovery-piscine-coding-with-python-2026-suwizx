from checkmate import checkmate

def main():
    board = """\
.....
..R..
.....
..K..
.....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()

"""
กระดานขนาด 5x5
.....
..R..
.....   
..K..
.....\

กระดานขนาด 3x3
Q..
...
..K\

"""

"""
กรณี Success
R...
....
K...
....\

....
K..Q
....
....\

....
.P..
K...
....\

"""


"""
กรณี Fail
R...
P...
K...
....\

.R..
....
K...
....\

....
PK..
....
....\

"""