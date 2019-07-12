class Animal:
    type = "Dog"

    def info(self):
        print("Message from class")
        print(self.type)

    def test(self, number):
        print(number)


animal = Animal()

print(animal.type)
animal.type = "Cat"
print(animal.type)

animal.info()
animal.test(5)
