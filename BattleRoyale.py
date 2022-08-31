import random
import time

contestants = ["Ananjay", "Noah", "Daniel", "Landon", "Sean", "Olivia", "Edward", "Jay", "Donald Trump", "Joe Biden", "Hillary Clinton", "Kim Jong Un", "Greta Thunberg", "Vladimir Putin"]
deaths = [""]
print(f"Contestants: {contestants}")
while len(contestants) > 1:
    print(f"Remaining contestants: {len(contestants)}")
    round_contestants = random.sample(contestants, 2)
    one = round_contestants[0]
    two = round_contestants[1]
    print(f"{one} vs. {two}!")
    time.sleep(2)
    winner = random.choice([one, two])
    loser = None
    if winner == one:
        loser = two
    else:
        loser = one
    print(f"{winner} wins!")
    contestants.remove(loser)
    print()
print(f"Winner is: {contestants[0]}!")
