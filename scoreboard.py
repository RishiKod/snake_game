from turtle import Turtle



class Score(Turtle):

    def __init__(self, updated_value):
        super().__init__()
        self.SCORE_COUNT = 0
        self.HIGH_SCORE = updated_value
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.SCORE_COUNT} High Score: {self.HIGH_SCORE}", False, align='center', font=('Courier', 20, 'normal'))

    def reset(self):
        int_highscore = int(self.HIGH_SCORE)
        if self.SCORE_COUNT > int_highscore:
            self.HIGH_SCORE = str(self.SCORE_COUNT)
        self.highscore_update()
        self.SCORE_COUNT = 0
        self.score_update()

    def highscore_update(self):
        with open('highscore.txt', mode='w') as file:
            file.write(self.HIGH_SCORE)

    def increase_score(self):
        self.SCORE_COUNT += 1
        self.score_update()

    # def game_over(self):
    #     self.color('white')
    #     self.penup()
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align='center', font=('Courier', 30, 'normal'))

