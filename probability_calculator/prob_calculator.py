import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs) -> None:
        
        #self.ball = 1
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
        
                
        if to_draw  > self.num_balls:
            return self.contents        
    
        for idx in range(to_draw):
            if len(self.contents) == 0:
                print("error!")
            
            draw_item = random.sample(self.contents, k = 1)            
            random_draw.append(draw_item[0])
            self.contents.remove(draw_item[0])

        return random_draw 

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball 
    # when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. 

    # To do this, we perform N experiments, count how many times M we get at least 2 red balls and 1 green ball, and estimate the probability as M/N. 
    # Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, 
    # and checking if we got the balls we were attempting to draw.
    #random.seed(num_experiments)
    match_counter = 0

    #draw_hat = hat.contents
    for ctr in range(num_experiments + 1):     
             
        draw_hat = copy.deepcopy(hat)
    # do draw
         
        result = draw_hat.draw(num_balls_drawn)
    # convert result into a dictionary {"blue":#,"green":#}
        result_compare = {}
        for item in result: 
            if item in result_compare:
                result_compare[item] = result_compare[item] + 1
            else: 
                result_compare[item] = 1

    # compare draw expected_balls={"blue":2,"green":1}
        match = False
        
        for key in expected_balls:
            
            if key not in result_compare:
                match = False            
            elif expected_balls[key] == result_compare[key]:
                match = True
            else:
                match = False

        if match == True:
        # if draw equals expected_ balls add to counter
            match_counter += 1            
            match = False            
        
        del draw_hat
    # print('Number of experiments count: ' + str(ctr))
    # print('Number of experiments param: ' + str(num_experiments))
    # print('Match counts: ' + str(match_counter))

    #Calculate the probability
    probability = match_counter/num_experiments

    return probability
