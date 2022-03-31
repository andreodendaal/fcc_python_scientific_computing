import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs) -> None:
        
        self.ball = 1
        #self.p_contents = args
        self.contents = []
        self.num_balls = 0
        #print(self.contents)
        for key, value in kwargs.items():
            for i in range(value):
                self.num_balls += 1
                self.contents.append(key) 
  
    def draw(self, to_draw):
        random_draw = []
        if to_draw > self.num_balls:
            return self.num_balls

        for idx in range(to_draw):
            draw_item = random.choice(self.contents)
            random_draw.append(draw_item)
            self.contents.remove(draw_item)
        
        return random_draw 

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball 
    # when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. 

    # To do this, we perform N experiments, count how many times M we get at least 2 red balls and 1 green ball, and estimate the probability as M/N. 
    # Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, 
    # and checking if we got the balls we were attempting to draw.
    expected_match = 0
    
        
    draw_hat = hat.contents
        # do draw
    result = hat.draw(num_balls_drawn)
        # compare draw

        # if draw equals expected_ balls add to counter
    expected_match += 1
    
    #Calculate the probability
    probability = expected_match/num_experiments

    return probability

# hat = Hat(red=5,blue=2)
# print(hat.draw(2))

# hat = Hat(red=3,blue=2)
# print(hat.contents) 