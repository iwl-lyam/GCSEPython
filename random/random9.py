import random
colours = ["BLUE", "YELLOW", "BROWN", "THE BEST COLOUR EVER."]
colour = random.choice(colours)

guess = False
while not guess:
    g = input("Guess a colour: ")
    if g != colour.lower():
        print("a witty answer which involves the correct colour e.g. 'I bet you are GREEN with envy' or 'You are probably feeling BLUE right now'. The correct answer is",colour.lower())
    else:
        print("'well done'")
        colour = random.choice(colours)
