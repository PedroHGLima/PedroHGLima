import numpy as np
import pandas

dados = pandas.read_csv("dados_grupo3.csv", usecols=["age", "sex", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh", "exng", "oldpeak", "slp", "caa", "thall"])
# acima sao lidos os dados em csv

original = np.array(dados)
transposta = original.transpose()
# entao eh calculada as matrizes original e transposta, para abaixo calcular Xt*X

matriz = np.matmul(transposta, original)


def decomposicaoEspectral(matriz):
    '''retorna a decomposicao espectral de uma matriz'''
    # calculo dos autovetores, para calcular a decomposicao espectral
    autovalores, autovetores = np.linalg.eig(matriz)

    # a espectral deve ser autovetores*matriz*autovetores^-1
    espectral = np.matmul(autovetores, matriz)
    espectral = np.matmul(espectral, np.linalg.inv(autovetores))

    return autovetores, espectral, np.linalg.inv(autovetores)


print(decomposicaoEspectral(matriz))
