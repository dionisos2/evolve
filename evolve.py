#!/bin/python

"""
Test the result of some evolutions mechanismes (http://lesswrong.com/lw/l5/evolving_to_extinction/)
"""
import random

class Mouse:
    """ A mice ! """
    def __init__(self, SD, sex = None, anti_SD = None):
        self.segregation_distorter = SD
        if anti_SD is None:
            self.anti_SD = random.randint(0, 1000) == 1
        else:
            self.anti_SD = anti_SD
        if sex is None:
            self.sex = random.choice(["male", "female"])
        else:
            self.sex = sex

class MouseGeneration:
    """ One generation of mouse """
    def __init__(self, number_of_mice_without_SD, number_of_mice_with_SD):
        self.reproductive_capacity = 5
        self.max_mice_number = 500
        mices = []
        for i in range(number_of_mice_without_SD):
            mices.append(Mouse(False))
        for i in range(number_of_mice_with_SD):
            mices.append(Mouse(True))
        self.set_mices(mices)

    def set_mices(self, mices):
        random.shuffle(mices)
        self.mices = mices[0:self.max_mice_number]

    def __str__(self):
        result = "-"*20 + "\n"
        result += "number of mice : " + str(self.number_of_mice()) + "\n"
        result += "number of male : " + str(self.number_of_male()) + "\n"
        result += "number of female : " + str(self.number_of_female()) + "\n"
        result += "number of mice with SD : " + str(self.number_of_mice_with_SD()) + "\n"
        result += "number of mice without SD : " + str(self.number_of_mice_without_SD()) + "\n"
        result += "number of mice with anti_SD : " + str(self.number_of_mice_with_anti_SD()) + "\n"
        result += "number of mice without anti_SD : " + str(self.number_of_mice_without_anti_SD()) + "\n"
        return result

    def number_of_mice(self):
        return len(self.mices)

    def number_of_male(self):
        return len([mice for mice in self.mices if mice.sex == "male"])

    def number_of_female(self):
        return len([mice for mice in self.mices if mice.sex == "female"])

    def number_of_mice_with_SD(self):
        return len([mice for mice in self.mices if mice.segregation_distorter])

    def number_of_mice_without_SD(self):
        return len([mice for mice in self.mices if not mice.segregation_distorter])

    def number_of_mice_with_anti_SD(self):
        return len([mice for mice in self.mices if mice.anti_SD])

    def number_of_mice_without_anti_SD(self):
        return len([mice for mice in self.mices if not mice.anti_SD])

    def get_next_generation(self):
        males = [mice for mice in self.mices if mice.sex == "male"]
        females = [mice for mice in self.mices if mice.sex == "female"]
        random.shuffle(males)
        random.shuffle(females)

        next_generation = []
        for (male, female) in zip(males, females):
            next_generation.extend(self.reproduce(male, female))

        next_mouse_generation = MouseGeneration(0, 0)
        next_mouse_generation.set_mices(next_generation)
        return next_mouse_generation

    def reproduce(self, male, female):
        children = []
        for i in range(self.reproductive_capacity):
            if male.anti_SD or female.anti_SD:
                children.append(Mouse(SD=male.segregation_distorter, anti_SD=True))
            else:
                if male.segregation_distorter:
                    children.append(Mouse(True, "male"))
                else:
                    children.append(Mouse(False))
        return children


mouse_generation = MouseGeneration(100, 10)

print(mouse_generation)
for i in range(20):
    mouse_generation = mouse_generation.get_next_generation()
    print(mouse_generation)

