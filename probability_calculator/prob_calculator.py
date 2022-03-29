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
    pass

hat = Hat(red=5,blue=2)
print(hat.draw(2))

# hat = Hat(red=3,blue=2)
# print(hat.contents) 