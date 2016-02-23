
import random
from genes.abstract_gene_float import AbstractGeneFloat

class PunisherGene(AbstractGeneFloat):
    """ The more empathetic, the more willing to take others into consideration """

    type_of_punishment = "no empathy"
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

        if self.value > choice_input["teammate_empathy"]:
            if PunisherGene.type_of_punishment == "no empathy":
                if choice_input["gain"] > 0:
                    return ({"accept_cooperation":True}, options)
                else:
                    return ({"accept_cooperation":False}, options)

            if PunisherGene.type_of_punishment == "revenge":
                if choice_input["teammate_gain"] > 0:
                    return ({"accept_cooperation":False}, options)
                else:
                    return ({"accept_cooperation":True}, options)
        else:
            return ({"accept_cooperation":options["choice"]}, options)


    @classmethod
    def name(cls):
        return "punisher gene"
