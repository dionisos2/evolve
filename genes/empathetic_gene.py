
import random
from genes.abstract_gene_float import AbstractGeneFloat

class EmpatheticGene(AbstractGeneFloat):
    """ The more empathetic, the more willing to take others into consideration """

    def __init__(self):
        super().__init__()
        self.value = random.uniform(0, 1)

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
        return 4

    def choose_handle(self, choice_input, options):
        choice_result = choice_input["gain"] + choice_input["teammate_gain"]*self.value
        if choice_result > 0:
            options["choice"] = True
            return ({"accept_cooperation":True}, options)
        else:
            options["choice"] = False
            return ({"accept_cooperation":False}, options)


    @classmethod
    def name(cls):
        return "empathetic gene"
