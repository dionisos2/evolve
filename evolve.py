#!/bin/python

"""
Test the result of some evolutions mechanismes (http://lesswrong.com/lw/l5/evolving_to_extinction/)
"""

from generation_manager import GenerationManager
from animal import Animal
from sd_gene import SDGene
from anti_sd_gene import Anti_SDGene




Animal.init_genes_class([SDGene, Anti_SDGene])

generation_manager = GenerationManager(100)

print(generation_manager)

for i in range(50):
    input()
    generation_manager.next_generation()
    print(generation_manager)
    if generation_manager.number_of_animals() == 0:
        print("DEAD")
        quit()

