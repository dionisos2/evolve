#!/bin/python

"""
Test how sex reproduction evolve to 50% male children and 50% female children
Whatever the starting configuration, if there is no extinction,
the equilibrium look like a gaussian curbe:
[0, 0, 0, 0, 0, 8, 55, 148, 298, 433, 448, 338, 197, 59, 16, 0, 0, 0, 0, 0, ]
"""

from generation_manager import GenerationManager
from animal import Animal
from genes.rate_of_male_gene import RateOfMaleGene
from genes.sd_gene import SDGene
from genes.anti_sd_gene import Anti_SDGene

Animal.init_genes_class([RateOfMaleGene])#, SDGene, Anti_SDGene])

generation_manager = GenerationManager(2000)

print(generation_manager)

for i in range(5000):
    input()
    generation_manager.next_generation()
    print(generation_manager)
    if generation_manager.number_of_animals() == 0:
        print("DEAD")
        quit()

