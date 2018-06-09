#!/bin/python

"""
Test some hypothesis about fairness
"""
import random

from generation_manager import GenerationManager
from animal import Animal
from genes.compromise_gene import CompromiseGene

Animal.init_genes_class([CompromiseGene])

def action_callback(animal, animals):
    """ What happen in the environnement """
    assert isinstance(animal, Animal)
    teammate = random.randint(0, len(animals)-1)
    teammate_compromise = animals[teammate].genes["compromise gene"].value

    choice_input = {"teammate_compromise":teammate_compromise}

    choice_output = animal.choose(choice_input)

    if choice_output["accept_cooperation"]:
        rate = choice_output["rate"]
        animal.reproductive_capacity += 2*rate
        animals[teammate].reproductive_capacity += 5*(1-rate)
    else:
        animal.reproductive_capacity += -10
        animals[teammate].reproductive_capacity += -10
    return True

generation_manager = GenerationManager(500)
generation_manager.action_callback = action_callback

generation_manager.run(10)
