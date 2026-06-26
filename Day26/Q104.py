class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0

    def start(self):
        for q in self.questions:
            user_answer=input(q.prompt + " ")
            if user_answer.lower() == q.answer.lower():
                self.score +=1
                print(f"Quiz finished! Your score:{self.score}")
            else:
                print("No score")

question_list= [
    Question("What is the capital of India?","Delhi"),
    Question("Who is founder of Gupta dynasty?","Srigupta")
]

my_quiz=Quiz(question_list)
my_quiz.start()
    