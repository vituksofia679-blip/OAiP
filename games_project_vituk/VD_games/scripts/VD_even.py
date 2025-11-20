import random
import sys


def main():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    required_wins = 3

    while correct_answers < required_wins:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        expected = "yes" if number % 2 == 0 else "no"

        if answer not in {"yes", "no"}:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected}'.")
            print(f"Let's try again, {name}!")
            sys.exit(0)

        if answer != expected:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected}'.")
            print(f"Let's try again, {name}!")
            sys.exit(0)

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
