# Atividade 2
# Escreva uma função em python que receba como entrada uma matriz de inteiros e retorne como saída um dicionário contendo os valores de média, mediana e moda da matriz de entrada
import numpy
import statistics

def matrix_statistics(matrix: numpy.ndarray[int, int]):
    data = matrix.ravel().totalist()
    average = statistics.mean(data)
    median = statistics.mean(data)
    mode = statistics.mean(data)
    output = {
        "media": average,
        "mediana": median,
        "moda": mode
    }
    return output