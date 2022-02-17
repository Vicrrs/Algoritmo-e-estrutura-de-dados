

#Paradigma Imperativo

def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente


"""
Conceitos estruturais

Paradigma Orientado à Objeto

Classe - um conjunto de objetos com as mesmas características

Objeto - Representação do mundo real como um tipo de dado de uma classe

Construtor - é uma função criada implicitamente com o mesmo nome da classe

Atributo - São variaveis de uma classe
"""


#Paradigma orientado a objeto
class Paciente:
    #acessando o construtor
    
    def __init__(self, nome, idade, cpf, email): 
        #Self->se refere a ele mesmo do ingles, faz referencia aos atributos/ função da propai classe
        print("Acessei o construtor!")
        self.nome = nome 
        self.idade = idade 
        self.cpf = cpf
        self.email = email
        #atibutos  / #variaveis
        
        
#Reuso e coesão

""" 
Simulação de Eventos Discretos -> Paradigma Orientado à objetos

Relação -> Destacando funções e variáveis

---------------------------------------------------------------

Conceitos Estruturais

-Classe

Classe é a estrutura que abstrai um conjunto de objetos com características similares.
Definindo o comportamento dos seus objetos através das estruturas.

1 - Atributos
2 - Métodos

A classe define um tipo de dado abstrato 
 
"""

#Abstrção
#Reuso e Coesão
#Acoplamento, herança, polimorfismo, GAP semântico

""" 
Conceitos Fundamentais

-Abstração
Processo pelo qual se isolam atributos de um objeto, considerendo
os que certos grupos de objetos tenham em comum. 

-Reúso

Não existe pior prática em programação do que repetir código

"""



