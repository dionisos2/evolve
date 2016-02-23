
import random

from genes.abstract_gene import AbstractGene

class Animal:
    """
    Animal that can mutate and produce offsprings.
    Offsprings inherite the genes of their parents.
    """

    initialized = False

    def __init__(self):
        if not Animal.initialized:
            raise RuntimeError("You should call Animal.init_genes_class\
            before instanciating Animal.")

        # The default sex is random (50/50), we change it after, according to the experiment.
        self.sex = random.choice(["male", "female"])
        self.reproductive_capacity = 5
        self.genes = {}
        for gene_class in Animal.genes_class:
            self.genes[gene_class.name()] = gene_class()

    @classmethod
    def init_genes_class(cls, genes_class):
        """ The type of genes that the animals have in the experiment """
        if len(genes_class) > 0:
            # Just to see we got something that seem ok
            assert issubclass(genes_class[0], AbstractGene)
        cls.genes_class = genes_class
        cls.initialized = True

    def __str__(self):
        result = "-"*20 + "\n"
        result += "sex : " + self.sex + "\n"
        for gene in self.genes.values():
            result += gene.name() + " : " + str(gene.has_trait) + "\n"
        return result

    def inherit_sex(self, male_parent, female_parent):
        """ Set sex to male or female randomly (50/50), but some genes can influence that """
        self.sex = random.choice(["male", "female"])

        sorted_genes = sorted(self.genes.items(), key=lambda x: x[1].priority(), reverse=True)

        options = []
        for gene_item in sorted_genes:
            gene_name = gene_item[0]
            male_gene = male_parent.genes[gene_name]
            female_gene = female_parent.genes[gene_name]
            (self.sex, options) = self.genes[gene_name].__class__.inherit_sex_handle(self.sex, male_gene, female_gene, options)

    def inherit(self, male_parent, female_parent):
        """ The animal inherit genes form its parents """
        assert isinstance(male_parent, Animal)
        assert isinstance(female_parent, Animal)
        assert male_parent.sex == "male"
        assert female_parent.sex == "female"

        self.inherit_sex(male_parent, female_parent)

        for gene in self.genes:
            male_gene = male_parent.genes[gene]
            female_gene = female_parent.genes[gene]
            self.genes[gene].inherit(self.sex, male_gene, female_gene)

    def choose(self, choice_input):
        """ How the animal will behave according to his genes """
        sorted_genes = sorted(self.genes.items(), key=lambda x: x[1].priority(), reverse=True)

        options = {}
        for gene_item in sorted_genes:
            gene_name = gene_item[0]
            (choice, options) = self.genes[gene_name].choose_handle(choice_input, options)
        return choice

    def mutate(self, number_of_times=1):
        """ Mutate all genes randomly """
        for i in range(number_of_times):
            for gene in self.genes:
                self.genes[gene].mutate(self.sex)

