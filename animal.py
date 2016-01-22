
import random

from genes.abstract_gene import AbstractGene

class Animal:
    """
    Traits_difficulty represent approximatively the probability to acquire
    a particular traits from scratch in minimun steps.

    Genes are what is heritable between generations, it represent
    how close the animal is to get a particular traits.
    """

    initialized = False

    def __init__(self):
        if not Animal.initialized:
            raise RuntimeError("You should call Animal.init_genes_class before instanciating Animal.")

        # The default sex is random (50/50), we change it after, according to the experiment.
        self.sex = random.choice(["male", "female"])

        self.genes = {}
        for gene_class in Animal.genes_class:
            self.genes[gene_class.name()] = gene_class()

    @classmethod
    def init_genes_class(cls, genes_class):
        """ The kind of genes of animal """
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


    def mutate(self, number_of_times = 1):
        """ add -1, 0 or 1 to each genes, randomly. (it can’t go below 0) """
        for i in range(number_of_times):
            for gene in self.genes:
                self.genes[gene].mutate(self.sex)
