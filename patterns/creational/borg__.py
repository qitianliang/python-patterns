class Borg:
    __name = "params in class"

    def __init__(self):
        self.name = self.__name

    def __repr__(self):
        return self.name

    @classmethod
    def cls_method(cls):
        return f"from class method:{cls.__name}"


borg = Borg()
print(borg)
print(Borg.cls_method())
print(borg._Borg__name)
print(Borg._Borg__name)