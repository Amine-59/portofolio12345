def gagnant(board):
    lignes = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for l in lignes:
        if board[l[0]] and board[l[0]] == board[l[1]] == board[l[2]]:
            return board[l[0]], list(l)
    return None, None

def minimax(board, est_ia):
    w, _ = gagnant(board)
    if w == "O": return  1
    if w == "X": return -1
    if all(board): return 0
    scores = []
    for i in range(9):
        if not board[i]:
            board[i] = "O" if est_ia else "X"
            scores.append(minimax(board, not est_ia))
            board[i] = None
    return max(scores) if est_ia else min(scores)

def meilleur_coup(board):
    best, move = -math.inf, None
    for i in range(9):
        if not board[i]:
            board[i] = "O"
            s = minimax(board, False)
            board[i] = None
            if s > best:
                best, move = s, i
    return move
