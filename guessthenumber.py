guessNumber=int(input("guess a number between 1 to 9"))
if(guessNumber>5):
    print("too high")
elif(guessNumber<5):
    print("too low")
else:
    print("correct")