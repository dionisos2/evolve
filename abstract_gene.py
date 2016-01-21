
import random
from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod

class AbstractGene:
    __metaclass__ = ABCMeta

    @classmethod
    def X_or_Y(cls):
        """ X or Y gene """
        raise NotImplementedError(str(cls) + " don’t implement X_or_Y method")

    @classmethod
    def priority(cls):
        raise NotImplementedError(str(cls) + " don’t implement priority method")

    @classmethod
    def name(cls):
        raise NotImplementedError(str(cls) + " don’t implement name method")

    @classmethod
    def inherit_sex_handle(cls, sex, male_gene, female_gene):
        return sex

    def mutate(self, sex):
        raise NotImplementedError(str(cls) + " don’t implement mutate method")

