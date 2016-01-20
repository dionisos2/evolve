#!/bin/python

from animal import Animal

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
