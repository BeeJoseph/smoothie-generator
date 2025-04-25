#This enables randomization when used
import random

#This a function that encases the whole code to make it easily reusuable at just the call of the function's name
def smoothie_generator():
    fruits = ["apple", "apricot", "banana", "blackberry", "blueberry", "canary melon", "cantaloupe", "cherry", "clementine", "cranberry", "currants", "dates", "dragon fruit", "durian", "figs","grapes", "grapefruit", "guava", "honeydew", "jack fruit", "kiwi","kumquat","lemon", "lime","lychee", "mandarin","mango", "nectarine", "orange", "papaya","passion fruit", "peach", "pear","persimmon", "pineapple", "plum", "pomegranate", "raspberries", "soursop", "star fruit", "strawberries", "tangelo", "tangerine", "watermelon"]
    liquids = ["almond milk", "oatmilk", "coconut milk", "milk"]
    proteins = ["chia seeds", "protein powder", "peanut butter", "almond butter", "greek yogurt", "instant oatmeal"]
    sweeteners = ["honey", "agave syrup", "maple syrup"]
    additions = ["cinnamon", "vanilla extract", "almond essence", "cocoa powder", "matcha powder"]
    sayings = ["Here is your unique smoothie: ", "Custom your smoothie using these: ", "Try out this kind of smoothie: ", "Here's a brand new flavah for ya: ", "Ooo, something new: ", "This may be the best smoothie you've ever had: ", "You'll never know if you don't try: "]
    sayings_end = ["Enjoy!", "Happy blending!", "What a combo!","Bet this will taste good!"]

    #This allows the user to filter out any ingredients they wouldn't want generated in their smoothie
    user_input = input("Any ingredients you DON'T want? (separate with commas): ")
    no_thanks = [item.strip().title() for item in user_input.split(",")]
    
    #This is a setup of lists for appending every item BUT the item the user doesn't want
    new_fruits = []
    new_liquids = []
    new_proteins = []
    new_sweeteners = []
    new_additions = []

    """
    This is a loop that's basically saying: for every item in the 'fruits' list, if the item is not in the list of the user's unwanted items,
    then the item will be appeneded into a new list. 
    """
    for f in fruits:
        if f not in no_thanks:
            new_fruits.append(f)
            
    #The new list with the user's accepted items will replace the original list
    fruits = new_fruits
    
    
    for l in liquids:
        if l not in no_thanks:
            new_liquids.append(l)
            
    liquids = new_liquids
    
    for p in proteins:
        if p not in no_thanks:
            new_proteins.append(p)
    
    proteins = new_proteins

    for s in sweeteners:
        if s not in no_thanks:
            new_sweeteners.append(s)
    
    sweeteners = new_sweeteners
    
    for a in additions:
        if a not in no_thanks:
            new_additions.append(a)
    
    additions = new_additions


    #The random.choice randomly selects an item from the fruits list and saves it to the fruit1 and fruit2 variable
    fruit1 = random.choice(fruits)
    fruit2 = random.choice(fruits)

    #This keeps the randomly selected item from the fruit lists different. It's saying, when the item from the fruit2 variable is the same
    #as the item from the fruit1 variable, randomly reselect the item from the fruit2 variable
    while fruit2 == fruit1:
        fruit2 = random.choice(fruits)
    
    liquid = random.choice(liquids)
    protein = random.choice(proteins)
    sweetener = random.choice(sweeteners)
    addition = random.choice(additions)
    saying = random.choice(sayings)
    saying_end = random.choice(sayings_end)

    #The 'f' allows what's inside the variable to be printed, instead of just the variable's name. 
    #The .title() uppercases the first letter of the variable when printed out.
    print(f"\n{saying}\n")
    print(f"🍓 {fruit1.title()}")
    print(f"🍊 {fruit2.title()}")
    print(f"🥛 {liquid.title()}")
    print(f"💪 {protein.title()}")
    print(f"🍯 {sweetener.title()}")
    print(f"✨ {addition}")
    print(f"\n{saying_end}")

#The whole code above is inside a function, and smoothie_generator() calls that function
smoothie_generator()