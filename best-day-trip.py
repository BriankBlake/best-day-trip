import random

dest = ['Washington Dc', 'Santa Monica', 'Las Vegas', 'New York', 'France']
food = ['Weber Grille', 'The Capital Grille', 'In n out burger', 'Texas Longhorn', 'Burnt Toast']
trans = ['Jet', 'Car', 'Cruise Ship', 'Airplane', 'Amtrak']
ent = ['Sporting Event', 'Movies', 'Theme Park', ' Concerts', 'Theater']

welcome_message = 'If you want the best Day Trip planner, you came to the right place!'
print(welcome_message)

def pick_destination():
    random_destination = random.choice(dest)
    user_input = input(f"What do you think of {random_destination} as a good pick? 'yes' or'no': ")
    while user_input != "yes":
        random_destination = random.choice(dest)
        user_input = input(f"Do you think {random_destination} is a better pick? ")
    return random_destination


def pick_resturant():
    random_restaurant = random.choice(food)
    user_input = input(f"Does this {random_restaurant} sound like a good place to eat? 'yes' or 'no': ")
    while user_input != "yes":
        random_restaurant = random.choice(food)
        user_input = input(f"Awww! ok here is an other place {random_restaurant} does this work? ")
    return random_restaurant

def pick_transportation():
    random_transportation = random.choice(trans)
    user_input = input(f"I think you would love taveling by this way {random_transportation} what you think? 'yes' or 'no': ")
    while user_input != "yes":
        random_transportation = random.choice(trans)
        user_input = input(f"That one you didn't like here is an other great pick for you {random_transportation} how about this? ")
    return random_transportation
def pick_entertainment():
    random_entertainment = random.choice(ent)
    user_input = input(f"This would be a fun place {random_entertainment} what do you think? 'yes' or 'no': ")
    while user_input != "yes":
        random_entertainment = random.choice(ent)
        user_input = input(f"Oh ok how about this one {random_entertainment} instead? ")
    return random_entertainment

def confirm_day_trip(dest, food, trans, ent):
    thank_you_message = 'Thank you for letting me be part of you day trip plans!'

    print(f'I had pick out {dest}, you will be eating at {food}, you will be getting around by {trans}, you will end the night with {ent}!')
    user_input = input(f'Are you satisfied with these options? yes or no:')
    if user_input == 'yes':
        print(thank_you_message)
    else:
        if user_input == 'no':
            best_day_trip()

def best_day_trip():
    confirmed_destination = pick_destination()
    confirmed_restaurant = pick_resturant()
    confirmed_transportation = pick_transportation()
    confirmed_enterainment = pick_entertainment()
    confirm_day_trip(confirmed_destination, confirmed_restaurant, confirmed_transportation, confirmed_enterainment)




best_day_trip()
