from mpi4py import MPI
import M1
import M2
import Head

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
isFinished = False
comp = "x"
player = "o"
board = {1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "}

if rank == 0:
    if not isFinished:
        board = comm.recv(source=1, tag=0)
        move1 = M1.player1Move(board)

    comm.send(move1, dest=1, tag=1)
    print("Process 0 sent" + move1 + "to process 1")

elif rank == 1:

    while not isFinished:
        print("Player 1 playing ....")
        comm.send(board, dest=0, tag=0)
        player1m = comm.recv(source=0, tag=1)
        Head.InsertLetter(comp, player1m)
        Head.printBoard(board)
        print("Player 2 playing ...")
        comm.send(board, dest=2, tag=2)
        player2m = comm.recv(source=2, tag=3)
        Head.InsertLetter(player, player2m)
        Head.printBoard(board)

    print("Game Over")

elif rank == 2:
    if not isFinished:
        board = comm.recv(source=1, tag=2)
        move2 = M2.player2Move(board)

    comm.send(move2, dest=1, tag=3)
    print("Process 2 sent" + move2 + "to process 1")

comm.Barrier()  # Synchronize processes