# BlindChessy  
This is an under development program to practice blindfold chess. It uses Python-chess package to have a record of the board and projects the SVG data with Qt. Stockfish chess engine is used to play the moves.

## Requirements  
The following packages are needed to run BlindChessy,  
-Python3(Obviously)  
-PyQt5  
-Python-chess  
-SpeechRecognition  
-pyttsx3  
Every package can be installed by simple `pip3 install 'package_name'`  

## Drawbacks    
Until now it can predict the moves only 40-50% times and some moves are totally unrecognisable. For example, it reads 'Knight d5' as 'night d v' and it is not fixed yet.    


I'm planning to train my own model to train my own model only to recognise chess moves. 


**Any help will be appreciated. Thanks :)**