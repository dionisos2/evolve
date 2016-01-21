
import random
from abstract_gene_bool import AbstractGeneBool

class Anti_SDGene(AbstractGeneBool):
    """ The anti-SD trait cancel the segregation_distorter_trait. """

    @classmethod
    def X_or_Y(cls):
        return "X" #(male and female)

    @classmethod
    def emergence_rate(cls):
        return 0.0005

    @classmethod
    def equilibrium(cls):
        return 0.05

    @classmethod
    def priority(cls):
        return 1

    @classmethod
    def inherit_sex_handle(cls, sex, male_gene, female_gene):
        assert isinstance(male_gene, Anti_SDGene)
        assert isinstance(female_gene, Anti_SDGene)

        if male_gene.has_trait or female_gene.has_trait:
            return random.choice(["male", "female"])
        else:
            return sex

    @classmethod
    def name(cls):
        return "Anti-SD"
