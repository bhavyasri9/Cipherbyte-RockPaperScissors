from random import randint
ch=["Rock","Paper","Scissors"]
play=True
while play:
    pl=None
    co=ch[randint(0,2)]
    while pl not in ch:
        pl=input("Enter a Choice from Rock , Paper , or Scissors: ")
    print("player's choice: ",pl)
    print("computer's choice: ",co)
    if pl==co:
        print("It's a tie!!🤝")
    elif(
        (pl=='Rock' and co=='Scissors')or
        (pl=='Paper' and co=='Rock')or
        (pl=='Scissors' and co=='Paper')
    ):
        print("kudos!,you won the game🥳🎉")
    else:
        print("you lose😓. Try Again!")
    pa=input("Play Again? (y/n): ").lower()
    if not pa=="y":
        play=False
print("Thanks for playing!!🤗")
