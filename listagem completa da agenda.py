import sys
import pickle
from functools import total_ordering

def nulo_ou_vazio(texto):
    return texto == None or not texto.strip()


def valida_faixa_inteiro(pergunta, inicio, fim, padrão = None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrão != None:
                entrada = padrão
            valor = int(entrada)
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print(f"Valor inválido digitar entre {inicio} e {fim}")
            
            
def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    while True:
        