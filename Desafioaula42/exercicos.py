"""1- Faça um programa em que o usuário  digita dois vaores  e o resultado da soma  é exibido na tela"""

n1 = int(input('Digite um Valor:'))
n2 = int(input('Digite outro Valor:'))
s = n1 + n2
print('A soma  entre {} e {} é igual a {}!'.format(n1,n2,s))

"""2- faça um programa em que o usuario precisa  cadastrar, nome, idade, telefone e email, depois mostre os valores digitados na tela"""

nome = input('Digite o nome')
idade = input('Digite a idade')
telefone = input('Digite o telefone')
email = input('Digite o email')

print('nome: {}\nidade {}\ntelefone: {}\nemail:{}'.format(nome,idade,telefone,email))

"""3-faça um programa  no qual o usuario precisa cadastrar as informações de um produto : código , nome, quantidade e preço. No final o programa deve  mostrar as informações  cadastradas  e exibir o valor  total da compra"""

def cadastrar_produto():
    print("=== Cadastro de Produto ===")
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))

    return codigo, nome, quantidade, preco

def mostrar_produto(codigo, nome, quantidade, preco):
    print("\n=== Dados do Produto ===")
    print("Código:", codigo)
    print("Nome:", nome)
    print("Quantidade:", quantidade)
    print("Preço:", preco)

if __name__ == "__main__":
    codigo, nome, quantidade, preco = cadastrar_produto()
    mostrar_produto(codigo, nome, quantidade, preco)

    total = quantidade * preco
    print("\nValor Total da Compra:", total)


"""4- faça um programa um programa que converte centimetros em metros"""
def converter_para_metros(centimetros):
    metros = centimetros / 100
    return metros

if __name__ == "__main__":
    try:
        centimetros = float(input("Digite a quantidade em centímetros: "))
        metros = converter_para_metros(centimetros)
        print(f"{centimetros} centímetros equivalem a {metros:.2f} metros.")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido em centímetros.")


"""5- faça um programa que calcule a área  de um quadrado/retângulo"""

def calcular_area_quadrado(base, altura):
    area = base * altura
    return area

if __name__ == "__main__":
    try:
        base = float(input("Digite o valor da base do quadrado/retângulo: "))
        altura = float(input("Digite o valor da altura do quadrado/retângulo: "))

        area = calcular_area_quadrado(base, altura)
        print(f"A área do quadrado/retângulo é: {area:.2f} unidades quadradas.")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para a base e altura.")

