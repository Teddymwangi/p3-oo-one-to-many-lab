# In tests/test_owner_pet.py

from lib.owner import Owner
from lib.pet import Pet

def test_owner_pets():
    owner = Owner("John")
    pet1 = Pet("Max", "dog", owner)
    pet2 = Pet("Whiskers", "cat", owner)
    assert owner.pets() == [pet1, pet2]

def test_add_pet():
    owner = Owner("John")
    pet = Pet("Max", "dog")
    owner.add_pet(pet)
    assert pet.owner == owner

def test_sorted_pets():
    owner = Owner("John")
    pet1 = Pet("Max", "dog", owner)
    pet2 = Pet("Whiskers", "cat", owner)
    pet3 = Pet("Charlie", "bird", owner)
    sorted_pets = owner.get_sorted_pets()
    assert sorted_pets == [pet2, pet3, pet1]

def test_invalid_pet_type():
    try:
        pet = Pet("Max", "fish")
    except Exception as e:
        assert str(e) == "Invalid pet type. Must be one of: dog, cat, rodent, bird, reptile, exotic"
