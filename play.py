from nim import train, play

ai = train(10000)
while True:
    play(ai)
    x = input("Play again? (Y/n) ")
    if x.lower() == "n":
        break
