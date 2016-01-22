
import random
from genes.abstract_gene_float import AbstractGeneFloat

class PunisherGene(AbstractGeneFloat):
    """ The more empathetic, the more willing to take others into consideration """

    def __init__(self):
        super().__init__()
        self.value = 0#random.uniform(0, 1)

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

    def choose_handle(self, choice_input, options):
        type_of_punishment = "no empathy"

        if self.value > choice_input[2]:
            if type_of_punishment == "no empathy":
                if choice_input[0] > 0:
                    return ([True], options)
                else:
                    return ([False], options)

            if type_of_punishment == "revenge":
                if choice_input[1] > 0:
                    return ([False], options)
                else:
                    return ([True], options)
        else:
            return ([options["choice"]], options)


    @classmethod
    def name(cls):
        return "punisher gene"
