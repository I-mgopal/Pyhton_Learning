class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"

    def __repr__(self):
        return f"Animal(name={self.name!r})"

    def __len__(self):
        return len(self.name)

    def __del__(self):
        print(f"{self.name} has been deleted.")

obj = Animal("Lion")
print(str(obj))        # Outputs: Animal: Lion
print(repr(obj))       # Outputs: Animal(name='Lion')
print(len(obj))        # Outputs: 4
del obj                 # Outputs: Lion has been deleted.

