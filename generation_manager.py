
import random
from animal import Animal
from genes.abstract_gene_bool import AbstractGeneBool
from genes.abstract_gene_float import AbstractGeneFloat

class GenerationManager:
    """ A generation of animals """
    def __init__(self, number_of_animals):
        self.max_animal_number = number_of_animals
        self.action_callback = lambda animal, animals: False
        animals = []
        for i in range(number_of_animals):
            animal = Animal()
            animals.append(animal)

        self.set_animals(animals)

    def set_animals(self, animals):
        random.shuffle(animals)
        self.animals = animals[0:self.max_animal_number]

    def __str__(self):
        result = "-"*20 + "\n"
        result += "number of animals : " + str(self.number_of_animals()) + "\n"
        result += "number of males : " + str(self.number_of_male()) + "\n"
        result += "number of females : " + str(self.number_of_female()) + "\n"
        result += "reproduction capacity distribution : ["
        borne_sup = 20
        for i in range(0, borne_sup):
            result += str(self.number_of_animals_with_rc_between(i, i+1)) + ", "
        result += str(self.number_of_animals_with_rc_between(borne_sup, 10000)) + "]\n"

        for gene in Animal.genes_class:
            if issubclass(gene, AbstractGeneBool):
                number_with_trait = self.number_of_animals_with_trait(gene.name())
                result += "number of animals with " + gene.name() + " : " + str(number_with_trait)
                if self.number_of_animals() != 0:
                    result += " (" + str(round(100*number_with_trait/self.number_of_animals(), 1)) + "%)"
                    number_of_males_with_trait = len([animal for animal in self.animals if animal.genes[gene.name()].has_trait and animal.sex == "male"])
                    number_of_females_with_trait = number_with_trait - number_of_males_with_trait
                    result += "(males=" + str(number_of_males_with_trait) + ", females=" + str(number_of_females_with_trait) + ")\n"
                else:
                    result += "\n"
            else:
                result += gene.name() + " distribution : ["
                result += str(self.number_of_animals_with_gene_between(gene.name(), -100000, 1/20)) + ", "
                for i in range(1, 19):
                    result += str(self.number_of_animals_with_gene_between(gene.name(), i/20, (i+1)/20)) + ", "
                result += str(self.number_of_animals_with_gene_between(gene.name(), 19/20, 100000)) + "]"
                if self.animals:
                    average = sum([animal.genes[gene.name()].value for animal in self.animals])/len(self.animals)
                    result += " average = " + str(round(average, 3)) + "\n"
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
        return len([animal for animal in self.animals if animal.genes[gene_name].has_trait])

    def number_of_animals_with_rc_between(self, minimum, maximum):
        return len([animal for animal in self.animals if (animal.reproductive_capacity >= minimum and animal.reproductive_capacity < maximum)])

    def number_of_animals_with_gene_between(self, gene_name, minimum, maximum):
        return len([animal for animal in self.animals if (animal.genes[gene_name].value >= minimum and animal.genes[gene_name].value < maximum)])

    def actions(self, number_of_actions):
        """ What happen in the environnement between two generations """
        for i in range(number_of_actions):
            for animal in self.animals:
                result = self.action_callback(animal, self.animals)
                if not result:
                    raise RuntimeError("You should init generation_manager.action_callback")

    def run(self, actions_by_generation=0):
        """ Run the experiment ! """
        dead = False
        generation_number = 1
        print(self)
        while not dead:
            input()
            self.actions(actions_by_generation)
            print("generation number : " + str(generation_number))
            print(self)
            if self.number_of_animals() == 0:
                print("DEAD")
                dead = True
            else:
                generation_number += 1
            self.next_generation()

    def reproduce(self, male_parent, female_parent):
        assert isinstance(male_parent, Animal)
        assert isinstance(female_parent, Animal)
        assert male_parent.sex == "male"
        assert female_parent.sex == "female"

        children = []
        reproductive_capacity = round((male_parent.reproductive_capacity + female_parent.reproductive_capacity)/2, 0)
        if reproductive_capacity <= 0:
            return []

        for i in range(int(reproductive_capacity)):
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
