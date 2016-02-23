#!/bin/python

"""
Test the result of some evolutions mechanismes (http://lesswrong.com/lw/l5/evolving_to_extinction/)
"""

from generation_manager import GenerationManager
from animal import Animal
from genes.sd_gene import SDGene
from genes.anti_sd_gene import Anti_SDGene


Animal.init_genes_class([SDGene, Anti_SDGene])

generation_manager = GenerationManager(1000)

generation_manager.run()
