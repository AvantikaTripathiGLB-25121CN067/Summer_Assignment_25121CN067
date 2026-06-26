class NumberGuessingGame:
    def __init__(self,secret_number):
        self.secret_number=secret_number
        self.attempts=0

    def make_guess(self,guess):
        self.attempts+=1
        if guess<self.secret_number:
            return "Too Low"
        elif guess>self.secret_number:
            return "Too High"
        else:
            return "correct! This is the secret number."
        
game=NumberGuessingGame(secret_number=42)
print(game.make_guess(25))
print(game.make_guess(45))
            

