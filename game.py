import random

characterList = {1:"The Doctor", 2:"K9", 3:"River", 4:"The Master", 5:"Dalek"}
startPointList = {1:"TARDIS", 2:"Galifrey", 3:"Skaro", 4:"Earth", 5:"Wales"}

tasksOne = {
    1:"Leave the TARDIS and lock the door",
    2:"Leave the TARDIS and it fades away",
    3:"You sense the Doctor is near you",
    4:"The TARDIS appears in front of you..."
}

print("------Welcome to The Doctor Who Game-------")
print("Please choose your Character from the list below:")
for key, value in characterList.items():
    print(key, "for", value)
character = int(input())
if character == 1:
    print("You have full Time Lord Powers")
print("Please choose your Start Point from the list below:")
for key, value in startPointList.items():
    print(key, "for", value)
startPoint = input()

if character < 4:
    if character == 1 or character ==3:
        print(tasksOne[2])
    elif character == 2:
        print(tasksOne[1])
    else:
        print("What species are you???")
elif character > 3:
    if character == 4:
        print(tasksOne[3])
    elif character == 5:
        print(tasksOne[4])
    else:
        print("You are not recognised!!!")

tasksTwo = {
    1:"Walk into town and look for Donna",
    2:"Take out your Sonic Screwdriver and scan for disturbances",
    3:"Prepare for confrontation",
    4:"You smile and try the door to the TARDIS"
}

print("Please choose your reaction from the list:")
for key, value in tasksTwo.items():
    print(key, "for", value)
option = input()

if character < 4:
    choice = random.randint(1, 3)
    if character == 1 or character ==3:
        print(tasksTwo[choice])
    elif character == 2:
        print(tasksTwo[choice])
    else:
        print("What species are you???")
elif character > 3:
    choice = random.randint(2, 4)
    if character == 4:
        print(tasksTwo[choice])
    elif character == 5:
        print(tasksTwo[choice])
    else:
        print("You are not recognised!!!")