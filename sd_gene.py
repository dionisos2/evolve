
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
        return 2

    @classmethod
    def inherit_sex_handle(cls, sex, male_gene, female_gene):
        assert isinstance(male_gene, SDGene)
        assert isinstance(female_gene, SDGene)

        if male_gene.has_trait:
            return "male"
        else:
            return sex

    @classmethod
    def name(cls):
        return "Segregation Distorter"
