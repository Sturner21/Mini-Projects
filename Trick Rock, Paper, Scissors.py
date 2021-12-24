print("Please type in ALL lowercase.")
record = {'Wins': 0, 'Losses': 0, 'Ties': 0}

while True:
    x = input("Rock, Paper, or Scissors?:")
    if x == "rock":
        print("I win, I picked paper.")
        record['Losses'] +=1
            
    if x == "paper":
        print("I win, I picked scissors.")
        record['Losses'] +=1
            
    if x == "scissors":
        print("I win, I picked rock.")
        record['Losses'] +=1
    print(record)

