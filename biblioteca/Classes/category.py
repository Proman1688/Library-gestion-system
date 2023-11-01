class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subcategories = []

    def addSubCategory(self, subcategory):
        self.subcategories.append(subcategory)

    def getSubCategoriesCount(self):
        return len(self.subcategories)

    def __str__(self):
        return self.name

    def displayTree(self, indent=0):
        print('  ' * indent + str(self))
        for subcategory in self.subcategories:
            subcategory.displayTree(indent + 1)