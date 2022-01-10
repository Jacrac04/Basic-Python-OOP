# My first thought is that a quiz has questions that are all similar so I will have a questions class and I could add subclasses for different styles of questions. 
# I will also have a quiz class that will generate the questions and create the 'quiz'. 
# As the questions don't really exist without a quiz i will use composition.
# I will also create a player class to keep track of the players score and progress.
# The quiz class will have an association with hte player as we want it to be able to interact with the player class but we don't want them to be dependent as we may want the play to be able to different quizzes.


class Question():
    type_ = "Q"
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points
    def getQuestion(self):
        return self.question
    def checkAnswer(self, answer):
        return self.answer == answer
    def getPoints(self):
        return self.points

class MultipleChoiceQuestion(Question):
    type_ = "MC"
    def __init__(self, question, answer, points, choices):
        super().__init__(question, answer, points)
        self.choices = choices
    def getChoices(self):
        return self.choices

class Quiz():
    def __init__(self):
        self.questions = []
    
    def generateQuestion(self, type_, question, answer, points, choices = None):
        if type_ == "MC":
            self.questions.append(MultipleChoiceQuestion(question, answer, points, choices))
        elif type_ == "Q":
            self.questions.append(Question(question, answer, points))

    def runQuiz(self, player):
        for question in self.questions:
            print(question.getQuestion())
            player.addHighestPossiblePoints(question.getPoints())
            if question.type_ == "MC":
                for index, choice in enumerate(question.getChoices()):
                    print((str(index+1)) + ') ' + choice)
            answer = input("Your answer: ")
            if question.checkAnswer(answer):
                player.addPoints(question.getPoints())
                print("Correct! " + str(question.getPoints()) + " points added. You are on " + str(player.getScore()) + " out of " + str(player.getHighestPossiblePoints()) + " points.")
            else:
                print("Wrong answer.")   
            
    

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.highestPossibleScore = 0
    def addPoints(self, points):
        self.score += points
    def getScore(self):
        return self.score
    def addHighestPossiblePoints(self, points):
        self.highestPossibleScore += points
    def getHighestPossiblePoints(self):
        return self.highestPossibleScore


player1 = Player("Bob")
quiz1 = Quiz()
quiz1.generateQuestion("MC", "What is the capital of France?", "Paris", 10, ["Paris", "London", "Berlin", "Rome"])
quiz1.generateQuestion("Q", "What is the capital of England?", "London", 10)
quiz1.runQuiz(player1)