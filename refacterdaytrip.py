import random

dest = ['Washington Dc', 'Santa Monica', 'Las Vegas', 'New York', 'France']
food = ['Weber Grille', 'The Capital Grille', 'In n out burger', 'Texas Longhorn', 'Burnt Toast']
trans = ['Jet', 'Car', 'Cruise Ship', 'Airplane', 'Amtrak']
ent = ['Sporting Event', 'Movies', 'Theme Park', ' Concerts', 'Theater']

welcome_message = 'If you want the best Day Trip planner, you came to the right place!'
print(welcome_message)



def pick_feature(array_of_features):
    random_feature = random.choice(array_of_features)
    user_input = input(
        f"What do you think of {random_feature} as a good pick? 'yes' or'no': ")
    while user_input != "yes":
        random_feature = random.choice(array_of_features)
        user_input = input(f"Do you think {random_feature} is a better pick? ")
    return random_feature


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
    confirmed_destination = pick_feature(dest)
    confirmed_restaurant = pick_feature(food)
    confirmed_transportation = pick_feature(trans)
    confirmed_enterainment = pick_feature(ent)
    confirm_day_trip(confirmed_destination, confirmed_restaurant, confirmed_transportation, confirmed_enterainment)




best_day_trip()