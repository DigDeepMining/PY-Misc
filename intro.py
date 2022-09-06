hello = "Hello World, the weather today is Sunny and bright"
#print(f"{hello} with a chance of meatballs")
weatherTypes = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
errorCodes = {404:"Website cannot be found", 111:"Facebook is broken", 123:"Instagram has blown up", 555:"Elon Musk has broken Twitter"}
#print(weatherTypes)

print("----18/30 Club----")
print("Enter your User Name below:")
userName = input().lower()
print(userName)
print("Enter your Age")
age = int(input())
print(age)

if userName == "daniel" and age > 30:
    print("You are Banned")
else:
    print("You can come in")

"""
for key,value in errorCodes.items():
    print(f"{key} is the Error code for {value}")
"""
"""
for item in weatherTypes:
    #print(item)
    if item == "Sunny":
        print("It's going to be Sunny today so don't forget your Sun Cream")
    elif item == "Cloudy":
        print("It's cloudy today so it will be dull so wear a bright shirt")
    elif item == "Rainy":
        print("It's going rain so take your Brolly")
    elif item == "Snowy":
        print("Today is going to be a build a snow man day")
    else:
        print("We have no idea waht the weather is today")
"""
match userName:
    case "daniel":
        print("Your username is on a block list")
    case "camille":
        print("you have access")