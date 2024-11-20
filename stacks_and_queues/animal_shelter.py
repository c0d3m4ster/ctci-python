import unittest

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.arrival_time = None

class AnimalShelter:
    def __init__(self):
        self.dogs = []  # List to hold dogs
        self.cats = []  # List to hold cats
        self.order = 0  # Timestamp for arrival time

    def enqueue(self, animal):
        animal.arrival_time = self.order
        self.order += 1
        if animal.species == 'dog':
            self.dogs.append(animal)
        elif animal.species == 'cat':
            self.cats.append(animal)
        else:
            raise ValueError("Animal must be a dog or a cat.")

    def dequeue_any(self):
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            return self.dequeue_cat()
        if not self.cats:
            return self.dequeue_dog()
        
        # Compare arrival times to determine which animal to dequeue
        if self.dogs[0].arrival_time < self.cats[0].arrival_time:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.pop(0) if self.dogs else None

    def dequeue_cat(self):
        return self.cats.pop(0) if self.cats else None

# Unit Tests
class TestAnimalShelter(unittest.TestCase):

    def setUp(self):
        self.shelter = AnimalShelter()

    def test_enqueue_and_dequeue_any(self):
        dog1 = Animal("Rex", "dog")
        cat1 = Animal("Whiskers", "cat")
        
        self.shelter.enqueue(dog1)
        self.shelter.enqueue(cat1)

        # Dequeue any should return Rex first since he was added first
        adopted_animal = self.shelter.dequeue_any()
        self.assertEqual(adopted_animal.name, "Rex")

    def test_dequeue_dog(self):
        dog1 = Animal("Rex", "dog")
        dog2 = Animal("Fido", "dog")
        
        self.shelter.enqueue(dog1)
        self.shelter.enqueue(dog2)

        adopted_animal = self.shelter.dequeue_dog()
        self.assertEqual(adopted_animal.name, "Rex")

    def test_dequeue_cat(self):
        cat1 = Animal("Whiskers", "cat")
        cat2 = Animal("Tom", "cat")
        
        self.shelter.enqueue(cat1)
        self.shelter.enqueue(cat2)

        adopted_animal = self.shelter.dequeue_cat()
        self.assertEqual(adopted_animal.name, "Whiskers")

    def test_empty_shelter(self):
        adopted_animal = self.shelter.dequeue_any()
        self.assertIsNone(adopted_animal)

if __name__ == '__main__':
    unittest.main()