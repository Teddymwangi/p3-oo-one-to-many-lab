# In lib/owner.py

from .pet import Pet

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet to an Owner")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda x: x.name)
        return sorted_pets
