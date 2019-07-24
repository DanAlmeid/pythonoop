import datetime
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def setNome(self, nome):
        self.nome = nome
    def setIdade(self , idade):
        self.idade = idade

class Pet(Pessoa):
    
    def __init__(self, nome_pet, nasc_pet, nome, idade):
        super().__init__(nome, idade)
        self.nome_pet = nome_pet
        self.nasc_pet = nasc_pet
    def getNomePet(self):
        return self.nome_pet
    def getNascPet(self):
        return self.nasc_pet
    def setNomePet(self, nome_pet):
        self.nome_pet = nome_pet
    def setNascPet(self, nasc_pet):
        nasc_pet = nasc_pet.strptime(nasc_pet, '%d/%m/%y').year()
        self.nasc_pet = nasc_pet
    

pessoa = Pessoa('Danilo', 21)
pet = Pet('Kachorro','20/03/2019','Danilo',21)
print(pet.getNascPet())