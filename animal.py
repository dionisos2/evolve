
import math
import random

class Animal:
    """
    Traits_difficulty represent approximatively the probability to acquire
    a particular traits from scratch in minimun steps.

    Genes are what is heritable between generations, it represent
    how close the animal is to get a particular traits.
    """
    traits_difficulty = {}
    # The segregation_distorter trait make the sigling all males.
    traits_difficulty["segregation_distorter"] = 0.001
    # The anti-SD trait cancel the segregation_distorter_trait
    traits_difficulty["anti-SD"] = 0.01
    genes_type = {}
    genes_type["segregation_distorter"] = "Y" #(male only)
    genes_type["anti-SD"] = "X" #(male and female)

    def __init__(self):
        # The default sex is random, we change it after according to the experiment.
        self.sex = random.choice(["male", "female"])
        self.genes = {}
        self.genes["segregation_distorter"] = 0.0
        self.genes["anti-SD"] = 0.0
        self.traits = {}
        self.init_traits()

    def __str__(self):
        result = "-"*20 + "\n"
        result += "sex : " + self.sex + "\n"
        for gene in sorted(self.genes):
            result += gene + " : " + str(self.genes[gene]) + "(" + str(self.traits[gene]) + ")\n"
        return result

    def init_traits(self):
        """ Determinate the traits of the animal, according to its genes """
        for gene in self.genes:
            # the probability P, to get the trait from scratch in the minimun number of steps N, is :
            # P = (1/3)^N = exp(ln(1/3)*N) ⇔
            # ln(P) = ln(1/3)*N ⇔
            # N = ln(P)/ln(1/3)
            P = self.traits_difficulty[gene]
            if P > 0:
                minimun_number_of_steps_scratch = math.log(P)/math.log(1/3)
            else:
                minimun_number_of_steps_scratch = float("inf")

            self.traits[gene] = (self.genes[gene] >= minimun_number_of_steps_scratch)

    def inherit_sex(self, male_parent, female_parent):
        m_anti_SD = male_parent.traits["anti-SD"]
        f_anti_SD = female_parent.traits["anti-SD"]
        m_SD = male_parent.traits["segregation_distorter"]

        if m_anti_SD or f_anti_SD:
            self.sex = random.choice(["male", "female"])
        else:
            if m_SD:
                self.sex = "male"
            else:
                self.sex = random.choice(["male", "female"])

    def inherit(self, male_parent, female_parent):
        """ The animal inherit genes form its parents """
        assert isinstance(male_parent, Animal)
        assert isinstance(female_parent, Animal)
        assert male_parent.sex == "male"
        assert female_parent.sex == "female"

        self.inherit_sex(male_parent, female_parent)

        for gene in male_parent.genes:
            if self.genes_type[gene] == "X":
                self.genes[gene] = (male_parent.genes[gene] + female_parent.genes[gene]) / 2
            else:
                if self.sex == "male":
                    self.genes[gene] = male_parent.genes[gene]
        self.init_traits()

    def mutate(self, number_of_times = 1):
        """ add -1, 0 or 1 to each genes, randomly. (it can’t go below 0) """
        for i in range(number_of_times):
            for gene in self.genes:
                self.genes[gene] += random.randint(-1, 1)
                if self.genes[gene] < 0:
                    self.genes[gene] = 0

        self.init_traits()
