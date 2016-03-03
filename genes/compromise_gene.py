
import random
from genes.abstract_gene_float import AbstractGeneFloat
from genes.abstract_gene import AbstractGene

class CompromiseGene(AbstractGeneFloat):
    """ The rate below which the deal is accepted """

    def __init__(self):
        super().__init__()
        # self.value = random.uniform(0, 1)
        if random.random() > 0.005:
            self.value = 0.18
        else:
            self.value = 0.78

    @classmethod
    def rate_of_change(cls):
        """ How fast the gene will change at each mutation """
        return 0.005

    @classmethod
    def X_or_Y(cls):
        """ X or Y gene """
        return "X"

    @classmethod
    def priority(cls):
        return 4

    def choose_handle(self, choice_input, options):
        teammate_compromise = choice_input["teammate_compromise"]
        self_compromise = self.value
        result = {}
        if teammate_compromise <= 0:
            teammate_compromise = 0.1
        if self_compromise <= 0:
            teammate_compromise = 0.1

        if (teammate_compromise + self_compromise) <= 1:
            result["accept_cooperation"] = True
            k = 1/(teammate_compromise + self_compromise)
            result["rate"] = self_compromise * k
        else:
            result["accept_cooperation"] = False

        return (result, {})

    def inherit(self, sex, male_gene, female_gene):
        assert isinstance(male_gene, AbstractGene)
        assert isinstance(female_gene, AbstractGene)

        if random.random() > 0.5:
            self.value = male_gene.value
        else:
            self.value = female_gene.value

    @classmethod
    def name(cls):
        return "compromise gene"
