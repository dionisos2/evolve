#!/bin/python

"""
Test the result of some evolutions mechanismes (http://lesswrong.com/lw/l5/evolving_to_extinction/)
"""

from generation_manager import GenerationManager


generation_manager = GenerationManager(100)

print(generation_manager)

for i in range(50):
    input()
    generation_manager.next_generation()
    print(generation_manager)
    if generation_manager.number_of_animals() == 0:
        print("DEAD")
        quit()

