# Beckett/Yámato Lutton
# Lab 3

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack_description(self):
        return f"attacks with {self.name} for {self.damage} damage"

class Character:
    def __init__(self, name, special_power):
        self.name = name
        self.special_power = special_power
        self.weapon = None

    def __str__(self):
        return f"I am {self.name}, a {self.__class__.__name__}"

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} {self.weapon.attack_description()}!"
        return f"{self.name} attacks with bare hands for 5 damage!"

    def get_status(self):
        weapon_info = self.weapon.name if self.weapon else "unarmed"
        return f"{self.name} the {self.__class__.__name__} - Weapon: {weapon_info}"

    def summon_power(self):
        raise NotImplementedError("Subclasses must implement summon_power()")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "Berserker Rage")
    def summon_power(self):
        return f"{self.name} unleashes {self.special_power}! Attack power doubled!"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Arcane Blast")
    def summon_power(self):
        return f"{self.name} channels {self.special_power}! Enemies are stunned!"

class Ranger(Character):
    """
    Task 1: Create a Subclass
    """
    def __init__(self, name):
        super().__init__(name, "Telekinesis")
    def summon_power(self):
        return f"{self.name} applies {self.special_power}! Rock hits enemy!"

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "Invisible Shield")
    def summon_power(self):
        return f"{self.name} creates an Invisible Shield!"

# Task 2: Create weapons
sword = Weapon("Sword", 20)
bow = Weapon("Bow", 40)

# print(sword.damage)

# Task 3: Build an army
army = [
    Ranger("Rick"),
    Warrior("Will"),
    Archer("Archie")
]

army[2].equip_weapon(bow)
print(army[2].get_status())
for character in army:
    character.equip_weapon(sword)
    print(character)
    print(character.get_status())
    print(character.summon_power())

# Task 4: Demonstrate weapon swapping
print(army[2].get_status())
army[2].equip_weapon(bow)
print(army[2].get_status())

# Task 5: Reflection
"""
Q1: Why is equipment modeled as composition (has-a) rather than inheritance (is-a)?

A1: Because a character has a weapon, a character is modeled with composition. It
is not modeled with inheritance because that would mean that the character was
a weapon.

Q2: What would go wrong if I used inheritance rather than composition?

A2: If I used inheritance, the character would be inaccurately modeled
as a weapon.
"""