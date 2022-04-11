from numpy import true_divide


def countPieces(generator, board):
    xCount = 0
    oCount = 0
    for piece in generator:
        if piece == 'x':
            xCount += 1
        elif piece == 'o':
            oCount += 1
    
    if xCount == 3:
        return 'x'
    elif oCount == 3:
        return 'o'

def countRow(row, board):
    return countPieces(board[row], board)

def countCol(coli, board):
    col = (row[coli] for row in board)
    return  countPieces(col, board)

# \
def countLeftDiag(board):
    col = (row[i] for i, row in enumerate(board))
    return  countPieces(col, board)

def countRightDiag(board):
    n = len(board)
    col = (row[n-i-1] for i, row in enumerate(board))
    return  countPieces(col, board) 

def hasWon(board):
    for i in range(3):
        s = countRow(i, board)
        if s != None:
            return s
        
        s = countCol(i, board)
        if s != None:
            return s
    
    s = countLeftDiag(board)
    if s != None:
        return s

    s = countRightDiag(board)
    if s != None:
        return s

    return None

class Node():
    pass

class State:
    def __init__(self,
        board = None,
        isMaxTurn = True,
    ) -> None:

        if board == None:
            board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
            ]

        self.board = board
        self.isMaxTurn = isMaxTurn


    def copy(self):
        return State( 
            board=[ row.copy() for row in self.board],
            isMaxTurn=self.isMaxTurn,
            )

def getAvailableMoves(state):
    return (
        (i,j) 
        for i, row in enumerate(state.board) 
            for j, piece in enumerate(row)
                if piece == ''
        )

def updateState(state: State, i, j):
    board = state.board
    if state.isMaxTurn:
        board[i][j] = 'x'
    else:
        board[i][j] = 'o'

def board_full(board):
    for row in board:
        for piece in row:
            if piece == '':
                return False

    return True

def print_state(state: State):
    print(state.isMaxTurn)
    for row in state.board:
        print(row)    

    print()
def minimaxValue(state:State, d) -> int:

    w = hasWon(state.board)
    if w != None:
        # print_state(state)
        if w == 'o':
            return -1 # last move 'o' won
        else: 
            return 1 # last move 'x' won

        raise Error("shouldn't be here")

    if board_full(state.board):
        # print_state(state)
        return 0

    else:
        vals = []
        ran = False
        for i, j in getAvailableMoves(state):
            ran = True
            nextState = state.copy()
            updateState(nextState, i, j)
            nextState.isMaxTurn = not nextState.isMaxTurn
            val = minimaxValue(nextState, d+1)
            vals.append(val)

        assert(ran)

        if state.isMaxTurn:
            return max(vals)
        else:
            return min(vals)

    raise Error("shouldn't be here")

if __name__ == "__main__":
    print(minimaxValue(State(), 0))



