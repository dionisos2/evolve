import random
import math
from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod
from genes.abstract_gene import AbstractGene

class AbstractGeneFloat(AbstractGene):
    """ A gene that give you a number between 0 and 1 """
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.value = 0.5 # we start with 50/50

    def gaussian(self, x):
        gmid = 0.005
        gmax = 0.15
        a = gmid/(gmax/gmid)
        b = 2*math.log(gmax/gmid)
        return a*math.exp(b*x)

    def mutate(self, sex):

        positive = random.random() > 0.5

        # self.value += random.uniform(-self.rate_of_change(), +self.rate_of_change())
        delta = self.gaussian(random.random())
        if positive:
            self.value += delta
        else:
            self.value -= delta

        if (sex == "female") and (self.__class__.X_or_Y() == "Y"):
            self.value = 0

        if self.value > 1:
            self.value = 1
        if self.value < 0:
            self.value = 0

    @classmethod
    def rate_of_change(cls):
        """ How fast the gene will change at each mutation """
        raise NotImplementedError(str(cls) + " don’t implement rate_of_change method")

    def inherit(self, sex, male_gene, female_gene):
        assert isinstance(male_gene, AbstractGene)
        assert isinstance(female_gene, AbstractGene)

        if self.__class__.X_or_Y() == "X":
            # self.value = (male_gene.value + female_gene.value) / 2
            if random.random() > 0.5:
                self.value = male_gene.value
            else:
                self.value = female_gene.value
        else:
            if sex == "male":
                self.value = male_gene.value
