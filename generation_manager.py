
import random
from animal import Animal

class GenerationManager:
    """ A generation of animals """
    def __init__(self, number_of_animals):
        self.reproductive_capacity = 5
        self.max_animal_number = 500
        animals = []
        for i in range(number_of_animals):
            animal = Animal()
            animal.mutate(5) # We start with random animals
            animals.append(animal)


        self.set_animals(animals)

    def set_animals(self, animals):
        random.shuffle(animals)
        self.animals = animals[0:self.max_animal_number]

    def __str__(self):
        result = "-"*20 + "\n"
        result += "number of animals : " + str(self.number_of_animals()) + "\n"
        result += "number of male : " + str(self.number_of_male()) + "\n"
        result += "number of female : " + str(self.number_of_female()) + "\n"

        for gene in Animal.genes_class:
            number_with_trait = self.number_of_animals_with_trait(gene.name())
            result += "number of animal with " + gene.name() + " : " + str(number_with_trait)
            if self.number_of_animals() != 0:
                result += " (" + str(round(100*number_with_trait/self.number_of_animals(), 0)) + "%)\n"
            else:
                result += "\n"

        return result

    def number_of_animals(self):
        return len(self.animals)

    def number_of_male(self):
        return len([animal for animal in self.animals if animal.sex == "male"])

    def number_of_female(self):
        return len([animal for animal in self.animals if animal.sex == "female"])

    def number_of_animals_with_trait(self, gene_name):
        return len([animal for animal in self.animals if animal.genes[gene_name].has_trait()])

    def reproduce(self, male_parent, female_parent):
        assert isinstance(male_parent, Animal)
        assert isinstance(female_parent, Animal)
        assert male_parent.sex == "male"
        assert female_parent.sex == "female"

        children = []
        for i in range(self.reproductive_capacity):
            child = Animal()
            child.inherit(male_parent, female_parent)
            child.mutate()
            children.append(child)
        return children

    def next_generation(self):
        males = [animal for animal in self.animals if animal.sex == "male"]
        females = [animal for animal in self.animals if animal.sex == "female"]
        random.shuffle(males)
        random.shuffle(females)

        next_generation = []
        for (male, female) in zip(males, females):
            next_generation.extend(self.reproduce(male, female))

        self.set_animals(next_generation)
