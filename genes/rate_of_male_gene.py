
import random
from genes.abstract_gene_float import AbstractGeneFloat

class RateOfMaleGene(AbstractGeneFloat):
    """ A gene that give you a trait or not """

    def __init__(self):
        super().__init__()
        # self.value = random.uniform(0, 1)
        self.value = 0.1
        # self.value = random.choice([0.2, 0.8])

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
        if value < 0:
            value = 0
        if value > 1:
            value = 1
        if random.random() < value:
            return ("male", options)
        else:
            return ("female", options)

    @classmethod
    def name(cls):
        return "rate of male gene"
