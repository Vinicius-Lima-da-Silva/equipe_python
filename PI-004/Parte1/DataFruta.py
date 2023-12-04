
from abc import ABC, abstractmethod
import os

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False
    

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        
        while True:
            qtdElementos = int(input("Digite o numero de elementos da lista de nomes : "))
            if qtdElementos <= 0:
                print("A Lista precisa ter tamanho mínimo de 1")
            else:
                break
            
        for i in range(1,qtdElementos+1):
            while True: 
                valor = input(f"Digite o {i} elemento : ")
                if valor=="":
                    print("Digite um nome válido!")
                    continue
                else:
                    self.__lista.append(valor)
                    break

    def mostraMediana(self):
        tamanhoDaLista= len(self.__lista)
        listaTemporaria = sorted(self.__lista)
        if tamanhoDaLista%2==0:
            indice = int(tamanhoDaLista / 2 - 1)
            print(f"Mediana é : {listaTemporaria[indice]}")
        else:
            indice = int(tamanhoDaLista / 2)
            print(f"Mediana é : {listaTemporaria[indice]}")


    def mostraMenor(self):
        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Alfabeticamente o menor é : {listaTemporaria[0]}")
        else:
            print("Lista está vazia!")

    def mostraMaior(self):
        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Alfabeticamente o maior é : {listaTemporaria[tamanhoDaLista-1]}")
        else:
            print("Lista está vazia!")
      
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        print("Lista em ordem:")
        for nome in listaOrdenada:
            print(nome)
        return listaOrdenada

    def __str__(self):
        for i in self.__lista:
            print(i)
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        
        while True:
            qtdElementos = int(input("Digite o numero de elementos da lista de datas : "))
            if qtdElementos <= 0:
                print("A Lista precisa ter tamanho mínimo de 1")
            else:
                break       
             
        for i in range(1,qtdElementos+1):
            while True: 
                dia = int(input(f"Digite o o dia {i} data : "))
                mes = int(input(f"Digite o o mês {i} data : "))
                ano = int(input(f"Digite o o ano {i} data : "))
                try:
                    dataNova = Data(dia,mes,ano)
                except ValueError as erro:
                    print(f"Erro : {erro}")
                else:
                    self.__lista.append(dataNova)
                    break
    
    def mostraMediana(self):    
        tamanhoDaLista= len(self.__lista)
        listaTemporaria = sorted(self.__lista)
        if tamanhoDaLista%2==0:
            indice = int(tamanhoDaLista / 2 - 1)
            print(f"Mediana é : {listaTemporaria[indice]}")
        else:
            indice = int(tamanhoDaLista / 2)
            print(f"Mediana é : {listaTemporaria[indice]}")
     
    def mostraMenor(self):
        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Menor Data é : {listaTemporaria[0]}")
        else:
            print("Lista está vazia!")
    
    def mostraMaior(self):
        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Maior Data é : {listaTemporaria[tamanhoDaLista-1]}")
        else:
            print("Lista está vazia!")
    
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        print("Lista em ordem:")
        for data in listaOrdenada:
            print(data)
    
    def modificar_datas(self):
        def modificar_data(data):
            if data.ano < 2019:
                data.dia = 1
            return data

        datas_anteriores_2019 = filter(lambda x: x.ano < 2019, self.__lista)
        self.__lista = list(map(modificar_data, datas_anteriores_2019))
    
    def __str__(self):
        for i in self.__lista:
            print(i)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):

        while True:
            qtdElementos = int(input("Digite o numero de elementos da lista de salários : "))
            if qtdElementos <= 0:
                print("A Lista precisa ter tamanho mínimo de 1")
            else:
                break
        for i in range(1,qtdElementos+1):
            while True: 
                valor = float(input(f"Digite o {i} elemento : "))
                if valor <= 0:
                    print("Digite um salário válido!")
                    continue
                else:
                    self.__lista.append(valor)
                    break
            
    def mostraMediana(self):

        tamanhoDaLista= len(self.__lista)
        listaTemporaria = sorted(self.__lista)
        if tamanhoDaLista%2==0:
            indice = int(tamanhoDaLista / 2 - 1)
            print(f"Mediana é : {listaTemporaria[indice]}")
        else:
            indice = int(tamanhoDaLista / 2)
            print(f"Mediana é : {listaTemporaria[indice]}")        

    def mostraMenor(self):

        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Menor Salário é : {listaTemporaria[0]}")
        else:
            print("Lista está vazia!")
        
    def mostraMaior(self):

        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Maior Salário é : {listaTemporaria[tamanhoDaLista-1]}")
        else:
            print("Lista está vazia!")
    
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        print("Lista em ordem:")
        for salario in listaOrdenada:
            print(salario)
        return listaOrdenada
    
    def reajustar_salarios(self, percentual):
        def aumentar_salario(salario):
            return salario * (1 + percentual)

        self.__lista = list(map(aumentar_salario, self.__lista))
        
    def calcular_custo_folha(self):
        return sum(self.__lista)
        
    def __str__(self):
        for i in self.__lista:
            print(i)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):

        while True:
            qtdElementos = int(input("Digite o numero de elementos da lista de idades : "))
            if qtdElementos <= 0:
                print("A Lista precisa ter tamanho mínimo de 1")
            else:
                break
        for i in range(1,qtdElementos+1):
            while True: 
                valor = int(input(f"Digite o {i} elemento : "))
                if valor <= 0:
                    print("Digite uma idade válida!")
                    continue
                else:
                    self.__lista.append(valor)
                    break

    def mostraMediana(self):

        tamanhoDaLista= len(self.__lista)
        listaTemporaria = sorted(self.__lista)
        if tamanhoDaLista%2==0:
            indice = int(tamanhoDaLista / 2 - 1)
            print(f"Mediana é : {listaTemporaria[indice]}")
        else:
            indice = int(tamanhoDaLista / 2)
            print(f"Mediana é : {listaTemporaria[indice]}")
    
    def mostraMenor(self):

        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Menor Idade é : {listaTemporaria[0]}")
        else:
            print("Lista está vazia!")

    def mostraMaior(self):

        tamanhoDaLista= len(self.__lista)
        if tamanhoDaLista > 0:
            listaTemporaria = sorted(self.__lista)
            print(f"Maior Idade é : {listaTemporaria[tamanhoDaLista-1]}")
        else:
            print("Lista está vazia!")

    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        print("Lista em ordem:")
        for idade in listaOrdenada:
            print(idade)

    def __str__(self):
        for i in self.__lista:
            print(i)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]


    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        print("___________________")

    for nome, salario in zip(nomes.listarEmOrdem(), salarios.listarEmOrdem()):
        print(f"Nome: {nome}, Salário: {salario}")

    salarios.reajustar_salarios(0.10)
    custo_total = salarios.calcular_custo_folha()
    print(f"Custo da folha de pagamento com salários reajustados: {custo_total}")

    datas.modificar_datas()

    # Exibindo as datas após a modificação
    datas.listarEmOrdem()


    

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()