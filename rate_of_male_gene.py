
import random
from abstract_gene_float import AbstractGeneFloat

class RateOfMaleGene(AbstractGeneFloat):
    """ A gene that give you a trait or not """

    def __init__(self):
        super().__init__()
        self.value = 0.1

    @classmethod
    def rate_of_change(cls):
        """ How fast the gene will change at each mutation """
        return 0.1

    @classmethod
    def X_or_Y(cls):
        """ X or Y gene """
        return "X"

    @classmethod
    def priority(cls):
        return 3

    @classmethod
    def inherit_sex_handle(cls, sex, male_gene, female_gene, options):
        value = (male_gene.value + female_gene.value)/2
        if random.random() < value:
            return ("male", options)
        else:
            return ("female", options)

    @classmethod
    def name(cls):
        return "rate of male gene"
