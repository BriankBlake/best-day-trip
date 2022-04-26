import random

dest = ['Washington Dc', 'Santa Monica', 'Las Vegas', 'New York', 'France']
food = ['Weber Grille', 'The Capital Grille', 'In n out burger', 'Texas Longhorn', 'Burnt Toast']
trans = ['Jet', 'Car', 'Cruise Ship', 'Airplane', 'Amtrak']
ent = ['Sporting Event', 'Movies', 'Theme Park', ' Concerts', 'Theater']

welcome_message = 'If you want the best Day Trip planner, you came to the right place!'
print(welcome_message)

def pick_destination():
    random_destination = random.choice(dest)
    user_input = input(f"What do you of {random_destination} as a good pick? 'yes' or'no': ")
    while user_input != "y":
        random_destination = random.choice(dest)
        user_input = input(f"Do you think {random_destination} is a better pick? ")
    return random_destination


def pick_resturant():
    random_restaurant = random.choice(food)
    user_input = input(f"Does this {random_restaurant} sound like a good place to eat? 'yes' or 'no': ")
    while user_input != "y":
        random_restaurant = random.choice(food)
        user_input = input(f"Awww! ok here is an other place {random_restaurant} does this work? ")
    return random_restaurant