import chess
import chess.svg
import chess.engine
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
import speech
import time
board=chess.Board()
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 750, 750)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 720, 720)

        self.chessboard = board

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def refresh(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
        self.repaint()

def find_pos(pos):
	pieces="ABCDEFGH"
	possition=0
	for j in pieces:
		if j==pos[0]:
			for i in range(1,9):
				if i==int(pos[1]):
					print(j+str(i)+" possition="+str(possition+(i-1)*8))
					return possition+(i-1)*8
				#possition+=1
		possition+=1

if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	window.show()
	engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")
	input('Press ENTER to start')
	while not board.is_game_over():
		result = engine.play(board, chess.engine.Limit(time=0.1))
		print(str(result.move))
		move=str(result.move)
		pos=move[0].upper()+move[1]
		print("pos="+pos)
		piece=find_pos(pos)
		print("piece[6]="+str(board.piece_at(6)))
		apiece=board.piece_at(piece)
		print("apiece="+str(apiece))
		move=str(apiece)+move[2]+move[3]
		print("move="+move)
		print(board)
		board.push(result.move)
		MainWindow.refresh(window)
		#time.sleep(5)
		speech.TexttoSpeak(move)
		input('Press ENTER to move')
		move=speech.SpeaktoText()
		print("Your move: "+move)
		board.push_san(move)
		MainWindow.refresh(window)
	engine.quit()

	#while True:
	#	move=input("Move for White: ")
	#	board.push_san(move)
	#	MainWindow.refresh(window)
	#	move=input("Move for Black: ")
	#	board.push_san(move)
	#	MainWindow.refresh(window)