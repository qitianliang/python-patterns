import random
from typing import Type
from abc import abstractmethod


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        sp_str = "woof"
        print(f"It speaks {sp_str}")

    # diff example is __str__
    def __repr__(self) -> str:
        return (f"Dog : {self.name}")


class Cat(Pet):
    def speak(self) -> None:
        sp_str = "meow"
        print(f"It speaks {sp_str}")

    # diff example is __str__
    def __repr__(self) -> str:
        return (f"Cat : {self.name}")


class PetShop:
    def __init__(self, pet_factory: Type[Pet]) -> None:
        self.pet_factory = pet_factory

    def buy_pet(self, name: str) -> Type[Pet]:
        # some diff
        pet = self.pet_factory(name)
        b_info = f"you bought a {pet}"
        print(b_info)
        return pet


# forget param: name
def random_pet(name: str) -> Type[Pet]:
    return random.choice([Dog, Cat])(name)


def main() -> None:
    """
	>>> cat_shop = PetShop(Cat)
	>>> pet = cat_shop.buy_pet("Lily")
	you bought a Cat : Lily
	>>> pet.speak()
	It speaks meow
    >>> random.seed(1234)
    >>> pet_shop = PetShop(random_pet)
    >>> for name in ["A","B"]:
    ...     
    ...     pet = pet_shop.buy_pet(name)
    ...     pet.speak()
	you bought a Cat : A
	It speaks meow
	you bought a Dog : B
	It speaks woof
    
	"""


if __name__ == "__main__":
    # does not take effect in doctest
    random.seed(1234)
    import doctest
    doctest.testmod()
