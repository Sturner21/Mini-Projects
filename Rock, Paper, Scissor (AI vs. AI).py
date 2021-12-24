import random
print("Computer 1 and Computer 2 will face off in 'Rock, Paper, Scissors'.")
o = ['rock', 'paper', 'scissors']
p = ['rock', 'paper', 'scissors']
while True:
    x = input("How many times should they compete?")
    z = int(x)
    record = {'Wins': 0, 'Losses':0, 'Ties': 0}

    for x in range(0, z):
        a = random.choice(o)
        b = random.choice(p)
        if a == b:
            record['Ties'] +=1
        else:
            if a == 'rock':
                if b == 'paper':
                    record['Losses'] +=1
                else:
                    record['Wins'] +=1
            if a == 'paper':
                if b == 'scissors':
                    record['Losses'] +=1
                else:
                    record['Wins'] +=1
            if a == 'scissors':
                if b == 'rock':
                    record['Losses'] +=1
                else:
                    record['Wins'] +=1
    print("The final record for Computer A was:")
    print(record)
