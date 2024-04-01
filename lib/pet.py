# In lib/pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        from .owner import Owner  # Importing Owner class locally
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Must be one of: {}".format(", ".join(self.PET_TYPES)))
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    @classmethod
    def get_all_instances(cls):
        return cls.all

    def set_owner(self, owner):
        from .owner import Owner  # Importing Owner class locally
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        self.owner = owner
