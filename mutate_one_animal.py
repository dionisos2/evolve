#!/bin/python
from animal import Animal
from sd_gene import SDGene
from anti_sd_gene import Anti_SDGene




Animal.init_genes_class([SDGene, Anti_SDGene])
female = Animal()
female.sex = "female"

male = Animal()
male.sex = "male"

male.mutate(10)
female.mutate(10)

child = Animal()
child.inherit(male, female)

print(male)
print(female)
print(child)
