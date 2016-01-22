import random
from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod
from genes.abstract_gene import AbstractGene

class AbstractGeneFloat(AbstractGene):
    """ A gene that give you a number between 0 and 1 """
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.value = 0.5 # we start with 50/50

    def mutate(self, sex):
        self.value += random.uniform(-self.rate_of_change(), +self.rate_of_change())
        if (sex == "female") and (self.__class__.X_or_Y() == "Y"):
            self.value = 0

    @classmethod
    def rate_of_change(cls):
        """ How fast the gene will change at each mutation """
        raise NotImplementedError(str(cls) + " don’t implement rate_of_change method")

    def inherit(self, sex, male_gene, female_gene):
        assert isinstance(male_gene, AbstractGene)
        assert isinstance(female_gene, AbstractGene)

        if self.__class__.X_or_Y() == "X":
            self.value = (male_gene.value + female_gene.value) / 2
            # if random.random() > 0.5:
            #     self.value = male_gene.value
            # else:
            #     self.value = female_gene.value
        else:
            if sex == "male":
                self.value = male_gene.value
