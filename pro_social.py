#!/bin/python

"""
Test some hypothesis about empathy
"""
import random

from generation_manager import GenerationManager
from animal import Animal
from genes.empathetic_gene import EmpatheticGene
from genes.punisher_gene import PunisherGene

PunisherGene.type_of_punishment = "no empathy"
Animal.init_genes_class([EmpatheticGene, PunisherGene])

def action_callback(animal, animals):
    """ What happen in the environnement """
    assert isinstance(animal, Animal)
    teammate = random.randint(0, len(animals)-1)

    gain = random.uniform(-15, 5)
    teammate_gain = random.uniform(-15, 5)
    teammate_empathy = animals[teammate].genes["empathetic gene"].value
    choice_input = {"gain":gain,
                    "teammate_gain":teammate_gain,
                    "teammate_empathy":teammate_empathy}

    choice_output = animal.choose(choice_input)
    if choice_output["accept_cooperation"]:
        animal.reproductive_capacity += gain
        animals[teammate].reproductive_capacity += teammate_gain
    return True

generation_manager = GenerationManager(200)
generation_manager.action_callback = action_callback

generation_manager.run(20)
