import speech_recognition as sr
import pyttsx3
def TexttoSpeak(move):
	if move[0]=='P' or move[0]=='p':
		move=move[1]+move[2]
	elif move[0]=='K' or move[0]=='k':
		move="King "+move[1]+move[2]
	elif move[0]=='Q' or move[0]=='q':
		move="Queen "+move[1]+move[2]
	elif move[0]=='B' or move[0]=='b':
		move="Bishop "+move[1]+move[2]
	elif move[0]=='R' or move[0]=='r':
		move="Rook "+move[1]+move[2]
	elif move[0]=='N' or move[0]=='n':
		move="Knight "+move[1]+move[2]
	try:
		eng=pyttsx3.init()
		eng.setProperty('rate',160)
		eng.say(move)
		eng.runAndWait()
	except Exception as e:
		print(e)

def isvalid(move,flag):
	try:
		pieces="abcdefgh"
		if len(move)<=3:
			#print("HI")
			if len(move)==3 and not(flag):
				#print("HI")
				start=1
				for j in pieces:
					if j==move[start]:
						for i in range(1,9):
							if i==int(move[start+1]):
								#print("HI")
								return move
			elif len(move)<3 and flag:
				start=0
				for j in pieces:
					if j==move[start]:
						for i in range(1,9):
							if i==int(move[start+1]):
								#print("HI")
								return move
		print('1 Invalid move! Try again!')
		input('Press ENTER to move')
		move=SpeaktoText()
		return move
	except Exception as e:
		print(e)
		print('2 Invalid move! Try again!')
		input('Press ENTER to move')
		move=SpeaktoText()
		return move

def SpeaktoText():
	flag=False
	r=sr.Recognizer()
	try:
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=0.2)
			audio=r.listen(source)
			text=r.recognize_google(audio)
			while len(text)<2 or text==None:
				print('3 Invalid move! Try again!')
				input('Press ENTER to move')
				audio=r.listen(source)
				text=r.recognize_google(audio)
		l=text.split()
		print(text)
		if l[0]=='Knight' or l[0]=='night':
			move='N'+l[1].lower()
			#print(move)
		elif l[0]=='King':
			move='K'+l[1].lower()
			#print(move[0]+l[1].lower())
		elif l[0]=='Queen':
			move='Q'+l[1].lower()
			#print(move[0])
		elif l[0][0]=='r' or l[0][0]=='R':
			move='R'+l[1].lower()
			#print(move[0])
		elif l[0]=='Bishop':
			move='B'+l[1].lower()
			#print(move[0])
		else:
			flag=True
			move=l[0].lower()
		move=isvalid(move,flag)
	except Exception as e:
		print("Exception occured! Try again!")
		input('Press ENTER to move')
		move=SpeaktoText()
	return move
if __name__=='__main__':
	move=SpeaktoText()
	print(move)