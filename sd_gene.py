
from abstract_gene_bool import AbstractGeneBool

class SDGene(AbstractGeneBool):
    """ The segregation_distorter(SD) trait make the sigling all males."""

    @classmethod
    def X_or_Y(cls):
        return "Y" #(male only)

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
    def inherit_sex_handle(cls, sex, male_gene, female_gene, options):
        assert isinstance(male_gene, SDGene)
        assert isinstance(female_gene, SDGene)

        if male_gene.has_trait and ("anti-SD" not in options):
            return ("male", options)
        else:
            return (sex, options)

    @classmethod
    def name(cls):
        return "Segregation Distorter"
