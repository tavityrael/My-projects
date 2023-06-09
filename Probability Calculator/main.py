import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            for i in range(count):
                self.contents.append(ball)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        balls_drawn = []
        for i in range(num):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls_drawn.append(ball)
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for ball, count in expected_balls.items():
        for i in range(count):
            expected_balls_list.append(ball)
    expected_count = expected_balls_list.count
    success_count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        drawn_count = []
        for ball in set(expected_balls_list):
            drawn_count.append(balls_drawn.count(ball))
        if all(c >= expected_count(ball) for ball, c in zip(set(expected_balls_list), drawn_count)):
            success_count += 1
    return success_count / num_experiments



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat = hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1)