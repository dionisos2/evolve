import random
from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod
from genes.abstract_gene import AbstractGene

class AbstractGeneBool(AbstractGene):
    """ A gene that give you a trait or not """
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self._has_trait = False

    @classmethod
    def emergence_rate(cls):
        """ What part of genes without the traits, will get the traits at each mutations """
        raise NotImplementedError(str(cls) + " don’t implement emergence_rate method")

    @classmethod
    def equilibrium(cls):
        """ Proportion of genes with the trait, at equilibrium (if the gene do nothing). """
        raise NotImplementedError(str(cls) + " don’t implement equilibrium method")

    @classmethod
    def extinction_rate(cls):
        """ What part of genes with the traits will lose it, at each mutation. """
        return (1/cls.equilibrium() - 1) * cls.emergence_rate()

    def mutate(self, sex):
        extinction_rate = self.__class__.extinction_rate()
        emergence_rate = self.__class__.emergence_rate()
        if self._has_trait:
            if random.random() < extinction_rate:
                self._has_trait = False
        else:
            if random.random() < emergence_rate:
                self._has_trait = True
        if (sex == "female") and (self.__class__.X_or_Y() == "Y"):
            self._has_trait = False

    def inherit(self, sex, male_gene, female_gene):
        assert isinstance(male_gene, AbstractGene)
        assert isinstance(female_gene, AbstractGene)

        if self.__class__.X_or_Y() == "X":
            if male_gene.has_trait == female_gene.has_trait:
                self._has_trait = male_gene.has_trait
            else:
                self._has_trait = (random.random() > 0.5)
        else:
            if sex == "male":
                self._has_trait = male_gene.has_trait

    @property
    def has_trait(self):
        return self._has_trait
