from nim import train, play
import os

def easy():
    ai = train(100)
    return ai
def medium():
    ai = train(1000)
    return ai
def hard():
    ai = train(10000)
    return ai

def main():
    while True:
        while True:
            try: 
                difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
                break
            except ValueError:
                print("\nInvalid input. Please enter integer numbers\n")
                return
        
        print("wait for a moment...")
        if difficulty == "easy":
            ai = easy()
        elif difficulty == "medium":
            ai = medium()
        elif difficulty == "hard":
            ai = hard()

        os.system("cls")

        while True:
            play(ai)

            select_difficulty = input("change difficulty? (Y/n) ")
            if select_difficulty.lower() == "y":
                break

            play_again = input("Play again? (Y/n) ")
            if play_again.lower() == "n":
                return

if __name__ == "__main__":
    main()