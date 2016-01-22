#!/bin/python

"""
Test some hypothesis about empathy
"""
import random

from generation_manager import GenerationManager
from animal import Animal
from genes.empathetic_gene import EmpatheticGene

Animal.init_genes_class([EmpatheticGene])

def action_callback(animal, animals):
    assert isinstance(animal, Animal)
    team_mate = random.randint(0, len(animals)-1)
    gain = random.uniform(-15, 5)
    team_mate_gain = random.uniform(-15, 5)
    choice_input = [gain, team_mate_gain]
    choice_output = animal.choose(choice_input)
    if choice_output[0]:
        animal.reproductive_capacity += gain
        animals[team_mate].reproductive_capacity += team_mate_gain
    return True

generation_manager = GenerationManager(200)
generation_manager.action_callback = action_callback

print(generation_manager)

for i in range(5000):
    input()
    generation_manager.next_generation()
    generation_manager.actions(20)
    print("generation number : " + str(i))
    print(generation_manager)
    if generation_manager.number_of_animals() == 0:
        print("DEAD")
        quit()

