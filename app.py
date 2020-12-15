from Question import Question

question_prompts = [
    "What color are apples?\n(a)Red/Green (b)Purple (c)Orange\n",
    "What color are bananas?\n(a)Teal(b)Magenta(c)Yellow\n",
    "What color are strawberries?\n(a)Yellow(b)Red(c)Blue\n"
    ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
    ]


def run_test(questions):
    score = 0
    for q in questions:
        result=input(q.prompt)
        if(result == q.answer):
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct.")

        

run_test(questions)
