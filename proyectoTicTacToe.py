board = [[1,2,3],[4,"X",6],[7,8,9]]


def DisplayBoard(board):
    print("+-------+-------+-------+\n|       |       |       |\n|   ",board[0][0],"   |   ",board[0][1],\
        "   |   ",board[0][2],"   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   "\
        ,board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |\n|       |       |       |\n+-------+-------\
+-------+\n|       |       |       |\n|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |\n|       \
|       |       |\n+-------+-------+-------+",sep="")



def EnterMove(board):
    a = int(input("Ingresa tu movimiento: "))
    for i in range(3):
        for j in range(3):
            if board[i][j] != a:
                continue
            else:
                board[i][j] = "O"
    return DisplayBoard(board)




listaVacios = [] ## la funcion es util para con esta lista generar los aleatorios
def MakeListOfFreeFields(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O" or board[i][j] == "X":
                continue
            else:
                listaVacios.append((i,j))




def VictoryFor(board):
    conteo = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                conteo += 1
        if board[i] == ["X","X","X"] or [board[0][0],board[1][0],board[2][0]] == ["X","X","X"]\
            or [board[0][1],board[1][1],board[2][1]] == ["X","X","X"] or [board[0][2],board[1][2],board[2][2]] == ["X","X","X"]\
            or [board[0][0],board[1][1],board[2][2]] == ["X","X","X"] or [board[0][2],board[1][1],board[2][0]] == ["X","X","X"]:
            return "¡Lo siento, Has perdido!"
        elif board[i] == ["O","O","O"] or [board[0][0],board[1][0],board[2][0]] == ["O","O","O"]\
            or [board[0][1],board[1][1],board[2][1]] == ["O","O","O"] or [board[0][2],board[1][2],board[2][2]] == ["O","O","O"]\
            or [board[0][0],board[1][1],board[2][2]] == ["O","O","O"] or [board[0][2],board[1][1],board[2][0]] == ["O","O","O"]:
            return "¡Felicidades, Has ganado!"
        elif conteo == 9:
            return "¡Es un empate!"



def DrawMove(board):
    from random import randrange
    miTupla = listaVacios[randrange(len(listaVacios))]
    board[miTupla[0]][miTupla[1]] = "X"
    return DisplayBoard(board)


DisplayBoard(board)
while True:
    if VictoryFor(board) == "¡Lo siento, Has perdido!" or VictoryFor(board) == "¡Felicidades, Has ganado!" or VictoryFor(board) == "¡Es un empate!":
        break
    EnterMove(board)
    VictoryFor(board)
    if VictoryFor(board) == "¡Lo siento, Has perdido!" or VictoryFor(board) == "¡Felicidades, Has ganado!" or VictoryFor(board) == "¡Es un empate!":
        break
    listaVacios = []
    MakeListOfFreeFields(board)
    DrawMove(board)
    VictoryFor(board)

print(VictoryFor(board))

