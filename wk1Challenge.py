import random
jokes=[
    ("Why do programmers prefer dark mode?", "Because light attracts bugs"),
    ("Why did the hacker break up with his girlfriend?", "She left her passwords everywhere"),
    ("Why did the cloud break up with the data center?", "Because it needed some space"),
    ("Why did the Linux admin break up with the Windows user?", "Too many arguments"),
    ("Why don’t skeletons fight each other?", "Because they don’t have the guts")
]
def joke_quiz():
    score = 0

    while True:
        play = input("\nDo you want to hear a joke? (yes/no): ").strip().lower()
        if play != "yes":
            print(f"\nYour final score: {score}")
            print("Thanks for playing! 😊")
            break  # Exit the game

        # Select a random joke
        question, answer = random.choice(jokes)
        print("\n" + question)  # Display the joke question

        attempts = 3
        while attempts > 0:
            user_answer = input("Your answer: ").strip().lower()

            if user_answer == answer.lower():  # Check if correct
                print("🎉 Correct! You get a point!")
                score += 1
                break  # Move to the next joke
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"❌ Incorrect. You have {attempts} attempt(s) left.")
                else:
                    print(f"😢 You lost! The correct answer was: {answer}")

# Start the quiz
joke_quiz()