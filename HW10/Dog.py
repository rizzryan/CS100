# Ryan Welch
# CS100 2017F Section 105
# HW 10, November 30th, 2017

class Dog(object):
    '''Represents the different attributes of a dog.'''

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricksList = []

    def name(self):
        return self.name

    def breed(self):
        return self.breed

    def tricks(self):
        return self.tricksList

    def teach(self, trick):
        self.trick = trick
        self.tricksList.append(self.trick)

        return self.name + ' knows the trick ' + self.trick

    def knows(self, trick):
        self.trick = trick

        if self.trick in self.tricksList:
            print('Yes, ' + self.name + ' knows the trick ' + self.trick + '.')
            return True
        else:
            print('No, ' + self.name + ' does not know the trick ' + self.trick + '. Perhaps, you should teach ' + self.name + ' ' + self.trick + '.')
            return False

    def species(self, species = 'Canis familiaris'):
        self.species = species
        return self.species
