print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").upper()
name2 = input("What is their name? \n").upper()

total_true = 0
total_love = 0
true_list = ["T", "R", "U", "E"]
love_list = ["L", "O", "V", "E"]


def find_true_total(name):
    global total_true
    for letter in name:
        if letter in true_list:
            total_true += 1


def find_love_total(name):
    global total_love
    for letter in name:
        if letter in love_list:
            total_love += 1

find_true_total(name1)
find_true_total(name2)
find_love_total(name1)
find_love_total(name2)


score = str(total_true) + str(total_love)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")