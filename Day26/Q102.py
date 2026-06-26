class VotingSystem:
    def __init__(self,min_age=18):
        self.min_age=min_age

    def check_eligibility(self,name,age):
        if age>=self.min_age:
            return f"Hello {name},you are eligibile for voting."
        else:
            return f"Sorry {name},you are not eligible for voting."
        
voter=VotingSystem()
print(voter.check_eligibility("Ashi",25))
print(voter.check_eligibility("Raju",16))