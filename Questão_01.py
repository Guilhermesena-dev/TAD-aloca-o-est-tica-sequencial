class Pilha: 
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.elementos = [None] * tamanho
        self.topo = -1 


    def inicializar_pilha(self):
        self.topo = -1 


    def pilha_vazia(self):
        return self.topo == -1
    
    def pilha_cheia(self):
        return self.topo == self.tamanho - 1 

 
    def empilha(self, elemento):
        if self.pilha_cheia():
            print("ERRO, PILHA CHEIA")
            return 
        self.topo += 1
        self.elementos [self.topo] = elemento 
 
    def desempilha(self):
        if self.pilha_vazia():
            print("ERRO, PILHA CHEIA")
            return None 
        elemento = self.elementos [self.topo]
        self.topo -= 1
        return elemento 

    def le_topo(self):
        if self.pilha_vazia():
            print("Erro, pilha vazia")
            return None
        return self.elementos[self.topo]    

    def imprimir(self):
        if self.pilha_vazia():
            print("pilha vazia")
            return
        for i in range(self.topo, -1, -1):
            print(self.elementos[i])

    def imprimir_reversa(self):
        if self.pilha_vazia():
            print("Pilha vazia.")
            return
        for i in range(0, self.topo + 1):
            print(self.elementos[i])

    def liberar(self):
        self.inicializar_pilha()
        print("Pilha liberada.")

    def eh_palindromo(self, string):
        self.inicializar_pilha()
        for char in string:
            self.empilha(char)
        inverso = ''.join([self.desempilha() for _ in range(len(string))])
        return string == inverso

    def elimina(self, elemento):
        aux_pilha = Pilha(self.tamanho)
        encontrado = False

        while not self.pilha_vazia():
            topo = self.desempilha()
            if topo == elemento:
                encontrado = True
                break
            aux_pilha.empilha(topo)

        while not aux_pilha.pilha_vazia():
            self.empilha(aux_pilha.desempilha())

        if encontrado:
            print(f"Elemento {elemento} removido.")
        else:
            print(f"Elemento {elemento} não encontrado.")
        return encontrado

    def pares_e_impares(self):
        pilha_pares = Pilha(self.tamanho)
        pilha_impares = Pilha(self.tamanho)

        while not self.pilha_vazia():
            elemento = self.desempilha()
            if elemento % 2 == 0:
                pilha_pares.empilha(elemento)
            else:
                pilha_impares.empilha(elemento)

        print("Pilha de pares:")
        pilha_pares.imprimir()
        print("Pilha de ímpares:")
        pilha_impares.imprimir()     


        ## TESTE:

if __name__ == "__main__":
        pilha = Pilha(10)

        pilha.empilha(1)
        pilha.empilha(2)
        pilha.empilha(3)
        pilha.empilha(4)
        pilha.empilha(5)

        print("Pilha original:")
        pilha.imprimir()

        print("\nImprimindo reversa:")
        pilha.imprimir_reversa()

        print("\nVerificando se 'arara' é palíndromo:")
        print(pilha.eh_palindromo("arara"))

        print("\nEliminando o elemento 3:")
        pilha.elimina(3)
        pilha.imprimir()

        print("\nSeparando em pares e ímpares:")
        pilha.empilha(1)
        pilha.empilha(2)
        pilha.empilha(3)
        pilha.empilha(4)
        pilha.empilha(5)
        pilha.pares_e_impares()

    


