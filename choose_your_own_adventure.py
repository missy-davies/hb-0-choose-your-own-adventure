# CHOOSE YOUR OWN ADVENTURE | WORLD TRAVEL

# Collect user input for name and set the scene
user = input("What is your name? ")
print(f"Ready to go on an adventure, {user}?")
print("Today you will be traveling across the world.")

# Collect more input from user and start the adventure 
friend = input("Who do you want to take with you? ")
print(f"Awesome! Alright {user}, you and {friend} will be leaving for a trip today, but where do you want to go?")

# Two way adventure beings- either France or Italy with two scenarios for each 
destination = int(input("Choose 1 for Italy or 2 for France. "))
if destination == 1:
    print("Fantastico! Just like that, you find yourselves in Italy, ready to eat and explore. But what's first?")
    print("Would you like to stop for lunch or head straight to the main piazza?")

    ita_activity = int(input("Type 1 for lunch and 2 for the piazza. "))
    if ita_activity == 1:
        print("Mamma mia, you're in luck! The country's best pizza parlour is just around the corner.")
        print(f"You and {friend} head inside and sit down for a fantastic meal of pizza margherita and wine galore.")
        print("La dolce vita indeed!")
    elif ita_activity == 2:
        print("You head to the main piazza and discover a myriad of fountains and elaborate statues.")
        print("Could this place be any more charming?!")
        print(f"You and {friend} jump in the fountain to cool off from the hot summer day. Che meraviglia!")
    else:
        print("Hmm, I'm not sure what you'd like to do here. Please re-read the instructions and start again!")
elif destination == 2:
    print(f"Oh la la! With a click of your fingers you and {friend} don your berets and are whisked off to France!")
    print(f"You and {friend} look at each other and revel in your french-ness. But wait, something is missing!")
    print("What do you need to complete your look?")
    print("Is it a baguette to put under your arm, or a striped shirt?")
    fra_activity = int(input("Type 1 for the baguette and 2 for the shirt. "))
    if fra_activity == 1:
        print(f"Excellent choice. {friend} was just starting to feel hungry, too.")
        print("You each buy une baguette and tuck it under your arms. Ah much better!")
    elif fra_activity == 2:
        print(f"Stunned you didn't think of this sooner, {friend} and you scuttle off to the nearest boutique.")
        print("You find the standard striped shirt and each buy one in your size.")
        print("While at the boutique, you spot a red scarf that really tops off the look and buy that too.")
        print("At last! The look is complete and it is...a masterpiece!")
    else:
        print("Hmm, I'm not sure what you'd like to do here. Please re-read the instructions and start again!")
else:
    print("Hmm, I don't know where that is. Please re-read the instructions and start again!")
