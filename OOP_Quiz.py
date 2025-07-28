import random


class Question:

    def __init__(self, mcqs=None):
        self.mcqs = mcqs if mcqs else [
            {
                "question": "Who is the current President of Russia?",
                "options": {
                    "A": "Vela Din Putin",
                    "B": "Imran Khan",
                    "C": "Donald Trump",
                    "D": "Nethan Yahuu",
                },
                "answer": "A",
            },
            {
                "question": "Which city is the trade city of Pakistan?",
                "options": {
                    "A": "Lahore",
                    "B": "Multan",
                    "C": "karachi",
                    "D": "Hydrabad",
                },
                "answer": "C",
            },
            {
                "question": "Which city is the capital city of Pakistan?",
                "options": {
                    "A": "Lahore",
                    "B": "Multan",
                    "C": "karachi",
                    "D": "Islamabad",
                },
                "answer": "D",
            },
        ]
        self.score = 0
        self.average = 0
        self.grade = None

    def logic(self):
        random.shuffle(self.mcqs)
        for mcq in self.mcqs:
            print("\n" + mcq['question'])

            for key, value in mcq['options'].items():
                print(f"{key}) {value}")

            user_input = input("Enter correct answer of question (A/B/C/D): ").upper().strip()
            if user_input not in ["A","B", "C", "D"]:
                print("Invalid option. Skiping this question.")
                continue

            if user_input == mcq['answer']:
                print("\nCorrect.")
                self.score += 1

            else:
                print(f"Wrong answer. Correct answer was: {mcq['answer']}")

        self.average = self.score / len(self.mcqs) * 100
        self.get_avg()
        self.get_result()

    def get_avg(self):
        if self.average >= 90:
            self.grade = "A+"
        elif self.average >= 80:
            self.grade = "A"
        elif self.average >= 70:
            self.grade = "B"
        elif self.average >= 60:
            self.grade = "C"
        elif self.average >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

    def get_result(self):
        print("=" * 10, "Result", "=" * 10)
        print(f"Percentage: {self.average:.2f}%")
        print(f"Score: {self.score} / {len(self.mcqs)}")
        print(f"Grade: {self.grade}")

while True:
    quiz = Question()
    quiz.logic()

    start_again = input("Would like to retake mcqs (yes/no): ").lower().strip()
    if start_again != "yes":
        print("Exiting..")
        break
