import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            copy = self.contents[:]
            self.contents.clear()
            return copy
        for i in range(num_balls):
            random_index = random.randint(0, len(self.contents)-1)
            drawn_balls.append(self.contents.pop(random_index))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            if ball in drawn_balls_dict:
                drawn_balls_dict[ball] += 1
            else:
                drawn_balls_dict[ball] = 1
        successful = True
        for key, value in expected_balls.items():
            if key not in drawn_balls_dict or drawn_balls_dict[key] < value:
                successful = False
                break
        if successful:
            num_successful += 1
    return num_successful/num_experiments
