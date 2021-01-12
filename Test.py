from Questions import Question
question_prompts = [
    "What is the square root of 121?\n(A) 15\n(B) 12\n(C) 11\n(D) 14\n\n",
    "What is 255/5 = ?\n(A) 21\n(B) 31\n(C) 41\n(D) 51\n\n",
    "What is 987-389 = ?\n(A) 598\n(B) 599\n(C) 600\n(D) 601\n\n",
    "Who is the main villain in Harry Potter?\n(A) Draco\n(B) Umbridge\n(C) Snape\n(D) Voldemort\n\n",
    "Who is the main villain in Final Fantasy 6?\n(A) Sephiroth\n(B) Kefka\n(C) Kuja\n(D) Ultimecia\n\n"
]

questions = [
    Question(question_prompts[0], "C"),
    Question(question_prompts[1], "D"),
    Question(question_prompts[2], "A"),
    Question(question_prompts[3], "D"),
    Question(question_prompts[4], "B"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct!")
            score += 1
        else:
            print("Nope! the correct answer is: " + str(question.answer) + "\n\n")
    print("Well done, you got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)