# mad_libs.py
# Mad Libs Story Generator with replay option and conditional endings

def play_mad_libs():
    print("\nWelcome to the Mad Libs Game! 🦁🐒")
    print("Fill in the blanks below to create your own story.\n")

    # Collect words from the user
    adjective1 = input("Enter an adjective (e.g., sunny, gloomy): ")
    adjective2 = input("Enter another adjective (e.g., funny, weird): ")
    adjective3 = input("Enter another adjective (e.g., majestic, fierce): ")
    adjective4 = input("Enter one more adjective (e.g., amazing, wild): ")
    animal1 = input("Enter a type of animal (e.g., monkey, tiger): ")
    animal2 = input("Enter another animal (e.g., lion, elephant): ")
    verb = input("Enter a verb ending in -ing (e.g., swinging, running): ")
    emotion = input("Enter an emotion (e.g., happy, scared, excited): ")

    # Conditional variation based on emotion
    if emotion.lower() in ["happy", "excited", "joyful"]:
        ending = "It was truly a day full of smiles and laughter!"
    elif emotion.lower() in ["scared", "terrified", "nervous"]:
        ending = "I almost ran away, but I managed to stay brave!"
    elif emotion.lower() in ["bored", "tired", "sleepy"]:
        ending = "I guess I should’ve stayed home with a cup of tea instead!"
    else:
        ending = "It was a day I’ll never forget — such a unique adventure!"

    # Build the story
    story = f"""
On a beautiful {adjective1} day, I went to the zoo. 
I saw a {adjective2} {animal1} {verb} from the trees. 
Then, I spotted a {adjective3} {animal2} lounging in the sun. 
What a {adjective4} experience it was — I felt so {emotion}!
{ending}
"""

    # Display the final story
    print("\n🎉 Here's your Mad Libs story! 🎉")
    print(story)


# Loop to replay
while True:
    play_mad_libs()

    # Ask if the user wants to play again
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("\nThanks for playing Mad Libs! See you next time! 👋")
        break
# mad_libs.py
# Mad Libs Story Generator with replay option and conditional endings

def play_mad_libs():
    print("\nWelcome to the Mad Libs Game! 🦁🐒")
    print("Fill in the blanks below to create your own story.\n")

    # Collect words from the user
    adjective1 = input("Enter an adjective (e.g., sunny, gloomy): ")
    adjective2 = input("Enter another adjective (e.g., funny, weird): ")
    adjective3 = input("Enter another adjective (e.g., majestic, fierce): ")
    adjective4 = input("Enter one more adjective (e.g., amazing, wild): ")
    animal1 = input("Enter a type of animal (e.g., monkey, tiger): ")
    animal2 = input("Enter another animal (e.g., lion, elephant): ")
    verb = input("Enter a verb ending in -ing (e.g., swinging, running): ")
    emotion = input("Enter an emotion (e.g., happy, scared, excited): ")

    # Conditional variation based on emotion
    if emotion.lower() in ["happy", "excited", "joyful"]:
        ending = "It was truly a day full of smiles and laughter!"
    elif emotion.lower() in ["scared", "terrified", "nervous"]:
        ending = "I almost ran away, but I managed to stay brave!"
    elif emotion.lower() in ["bored", "tired", "sleepy"]:
        ending = "I guess I should’ve stayed home with a cup of tea instead!"
    else:
        ending = "It was a day I’ll never forget — such a unique adventure!"

    # Build the story
    story = f"""
On a beautiful {adjective1} day, I went to the zoo. 
I saw a {adjective2} {animal1} {verb} from the trees. 
Then, I spotted a {adjective3} {animal2} lounging in the sun. 
What a {adjective4} experience it was — I felt so {emotion}!
{ending}
"""

    # Display the final story
    print("\n🎉 Here's your Mad Libs story! 🎉")
    print(story)


# Loop to replay
while True:
    play_mad_libs()

    # Ask if the user wants to play again
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("\nThanks for playing Mad Libs! See you next time! 👋")
        break
