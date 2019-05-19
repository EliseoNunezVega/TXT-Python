def main():
    meal= []
    checkcorrect = 'n'
    
    name = input("Hello, my name is Eliseo, I'll be your waiter for today. What is your name?:\n")
    print("You have a lovely name,", name)
    while checkcorrect == 'n':
        meal.append(input("What can I get for you?:\n"))
        checkdone = input("Good choice. Would you like anything else? (y/n):\n")
        while (checkdone == 'y' or checkdone == 'yes'):
            meal.append(input("What else can I get for you?:\n"))
            checkdone = input("Got it! And would you like anything else? (y/n):\n")
            continue

        print("Perfect! I have here an order for:")

        for x in meal:
            print(x)

        checkcorrect = input("Does the order sound correct? (y/n)")

        if checkcorrect == 'y' or checkcorrect == 'yes':
            print("Alright! I'll be out with your food shortly")
        elif checkcorrect == 'n' or checkcorrect == 'no':
            print("I'm so sorry! We'll start all over to make sure your order is correct")
            del meal[:]
            continue

main()
    
       
    
        
    
                 
                 
