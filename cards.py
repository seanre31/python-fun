import random

card_signs =['Heart','Club','Diamond','Spade']



num_gen = random.randint(1, 13)
sign_gen = random.choice(card_signs)
card_gen = num_gen, sign_gen



if num_gen == 1:
    print("Ace", "of", sign_gen)
elif num_gen == 11:
    print("Jack", "of", sign_gen)
elif num_gen == 12:
    print("Queen", "of", sign_gen)
elif num_gen == 13:
    print("King", "of", sign_gen)
elif 1 < num_gen <11:
    print(num_gen, "of", sign_gen)

u_guess = str(input("Guess whether the next card will be higher or lower: ")) 

num_gen2 = random.randint(1, 13)
sign_gen2 = random.choice(card_signs)
card_gen2 = num_gen2, sign_gen2


if num_gen2 == 1:
    print("Ace", "of", sign_gen2)
elif num_gen2 == 11:
    print("Jack", "of", sign_gen2)
elif num_gen2 == 12:
    print("Queen", "of", sign_gen2)
elif num_gen2 == 13:
    print("King", "of", sign_gen2)
elif 1 < num_gen2 <11:
    print(num_gen2, "of", sign_gen2)

    
if u_guess == "lower" and num_gen2 < num_gen:
    print("you win")
elif u_guess == "higher" and num_gen2 < num_gen:
    print("you lose")
elif u_guess == "lower" and num_gen2 > num_gen:
    print("you lose")
elif u_guess == "higher" and num_gen2 > num_gen:
    print("you win")



