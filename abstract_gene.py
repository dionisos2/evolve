import math
from abc import ABCMeta, abstractmethod, abstractproperty

class AbstractGene:
    __metaclass__ = ABCMeta
    minimun_number_of_steps_scratch = None

    def __init__(self):
        self.constructing_step = 0.0

    @classmethod
    def X_or_Y(cls):
        pass

    @classmethod
    def trait_difficulty(cls):
        pass

    @classmethod
    def get_minimun_number_of_steps_scratch(cls):
        if cls.minimun_number_of_steps_scratch == None:
            # the probability P, to get the trait from scratch in the minimun number of steps N, is :
            # P = (1/3)^N = exp(ln(1/3)*N) ⇔
            # ln(P) = ln(1/3)*N ⇔
            # N = ln(P)/ln(1/3)
            P = cls.trait_difficulty()
            if P > 0:
                cls.minimun_number_of_steps_scratch = math.log(P)/math.log(1/3)
            else:
                cls.minimun_number_of_steps_scratch = float("inf")

        return cls.minimun_number_of_steps_scratch


    def has_trait(self):
        result = self.constructing_step >= self.__class__.get_minimun_number_of_steps_scratch()
        return result
