import random
y = ["rock", "paper", "scissors"]
print("Please type in ALL lowercase.")
record = {'Wins': 0, 'Losses': 0, 'Ties': 0}

while True:
    z = random.choice(y)
    x = input("Rock, Paper, or Scissors?:")

    if z == x:
        print("Tie. I also picked {}.".format(z))
        record['Ties'] +=1
    else:
        if z == "rock":
            if x == "paper":
                print("You win, I picked rock.")
                record['Wins'] +=1
            else:
                print("I win, I picked rock.")
                record['Losses'] +=1
            
        if z == "paper":
            if x == "scissors":
                print("You win, I picked paper.")
                record['Wins'] +=1
            else:
                print("I win, I picked paper.")
                record['Losses'] +=1
            
        if z == "scissors":
            if x == "rock":
                print("You win, I picked scissors.")
                record['Wins'] +=1
            else:
                print("I win, I picked scissors.")
                record['Losses'] +=1
    print(record)
