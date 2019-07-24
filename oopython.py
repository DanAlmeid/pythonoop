from datetime import date, datetime
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
        nasc_pet = datetime.strptime(nasc_pet, '%d/%m/%Y').date()
        self.nasc_pet = nasc_pet
    def getNomePet(self):
        return self.nome_pet
    def getNascPet(self):
        return self.nasc_pet
    def setNomePet(self, nome_pet):
        self.nome_pet = nome_pet
    def setNascPet(self, nasc_pet):
        nasc_pet = datetime.strptime(nasc_pet, '%d/%m/%Y').date()
        self.nasc_pet = nasc_pet
    def idadePet(self):
        hoje = datetime.today().date()
        if self.nasc_pet.year == hoje.year:
            idade = hoje.month - self.nasc_pet.month
            print('O pet tem {} mes(es)' .format(idade))
        elif self.nasc_pet.year < hoje.year and (hoje.month - self.nasc_pet.month) >= 0:
            idade = hoje.year - self.nasc_pet.year
            print('O pet tem {} ano(s)' .format(idade))
        else:
            idade = hoje - self.nasc_pet
            idade = idade.days/30
            print('O pet tem  {} mes(es)' .format(int(idade)))

pessoa = Pessoa('Danilo', 21)
pet = Pet('Kachorro','20/8/2018','Danilo',21) 
print(pet.idadePet())