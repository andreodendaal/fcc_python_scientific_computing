import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs) -> None:
        
        self.ball = 1
        #self.p_contents = args
        self.contents = []
        #print(self.contents)
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key) 
  
    # def contents(self):
    #     #print("called contents!")
    #     # Iterate through parameters
        
    #     #print(self.content)

    #     return self.content     

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
# hat = Hat(red=3,blue=2)
# print(hat.contents) 