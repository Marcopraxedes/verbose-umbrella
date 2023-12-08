class Carro:

    def __init__(self):
        self.cor = 'Preto'
        self.marca = 'Volkswagem'
        self.modelo = 'Golf'
        self.ligado = False
        self.andando = False

        print(self.status())     

    def ligar_motor(self):
        print('Ligue o carro')
        self.ligado = True
        self.andando = False
        print(self.status())

    def andar(self):
        print('Pode andar')
        self.ligado = True
        self.andando = True
        print(self.status())

    def parar(self):
        print('Pode parar')
        self.ligado = True
        self.andando = False
        print(self.status())

    def desligar_motor(self):
        print('Desligue o Carro')
        self.ligado = False
        self.andando = False
        print(self.status())
        
    def status(self):
        if self.ligado:
            print('O Carro está Ligado')
        else:
            print('O Carro está Desligado')
        if self.andando:
            print('O Carro está Andando')
        else:
            print('O Carro está Parado')
     

carrinho = Carro()
print(carrinho.marca)
print(carrinho.modelo)
print(carrinho.cor)
carrinho.ligar_motor()
carrinho.andar()
carrinho.parar()
carrinho.desligar_motor()