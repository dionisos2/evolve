#!/bin/python

"""
Test how sex reproduction evolve to 50% male children and 50% female children
"""

from generation_manager import GenerationManager
from animal import Animal
from rate_of_male_gene import RateOfMaleGene

Animal.init_genes_class([RateOfMaleGene])

generation_manager = GenerationManager(500)

print(generation_manager)

for i in range(5000):
    input()
    generation_manager.next_generation()
    print(generation_manager)
    if generation_manager.number_of_animals() == 0:
        print("DEAD")
        quit()

