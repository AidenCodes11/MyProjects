import random, time

winning = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

if __name__ == "__main__":
    while True:
        user = input("Rock, paper, or scissors? ").lower().strip()
        while user not in ["rock", "paper", "scissors"]:
            user = input("You have to pick rock, paper, or scissors! ").lower().strip()
        chosen = random.choice(["rock", "paper", "scissors"])
        print("I pick", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(f" {chosen}!")
        if chosen == user:
            print("Tie!")
        elif winning[chosen] == user:
            print("I win!")
        elif winning[user] == chosen:
            print("You win!")
        print("Lets play again!\n")
