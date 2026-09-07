import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is 15 * 4?",
        "options": ["A. 45", "B. 50", "C. 60", "D. 75"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A. list", "B. loop", "C. function", "D. command"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A. ^", "B. **", "C. //", "D. %%"],
        "answer": "B"
    }
]


def ask_question(question_number, question):
    print("\n" + "=" * 50)
    print(f"Question {question_number}")
    print("=" * 50)

    print(question["question"])

    for option in question["options"]:
        print(option)

    while True:
        answer = input("\nYour answer: ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Invalid answer. Please enter A, B, C, or D.")


def show_result(score, total):
    percentage = (score / total) * 100

    print("\n" + "=" * 50)
    print("                 QUIZ RESULT")
    print("=" * 50)

    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {total - score}")
    print(f"Total Questions : {total}")
    print(f"Percentage      : {percentage:.2f}%")

    if percentage >= 90:
        print("Grade           : A+")
        print("Excellent! 🏆")

    elif percentage >= 75:
        print("Grade           : A")
        print("Very Good! 🎉")

    elif percentage >= 60:
        print("Grade           : B")
        print("Good job! 👍")

    elif percentage >= 50:
        print("Grade           : C")
        print("Keep practicing!")

    else:
        print("Grade           : F")
        print("Better luck next time!")

    print("=" * 50)


def start_quiz():

    print("\n" + "*" * 50)
    print("             PYTHON QUIZ GAME")
    print("*" * 50)

    name = input("\nEnter your name: ")

    # Randomize the questions
    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    score = 0

    # Ask 5 random questions
    selected_questions = quiz_questions[:5]

    for number, question in enumerate(selected_questions, start=1):

        user_answer = ask_question(number, question)

        if user_answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(
                f"❌ Wrong! "
                f"The correct answer was {question['answer']}."
            )

    print(f"\nWell done, {name}!")

    show_result(score, len(selected_questions))


def main():

    while True:

        start_quiz()

        print("\nDo you want to play again?")
        choice = input("Enter Y/N: ").strip().upper()

        if choice != "Y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()