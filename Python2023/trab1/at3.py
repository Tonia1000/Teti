# Atividade 3
# Escreva um algoritmo que receba uma matriz de inteiros como entrada e retorne um array contendo as medianas de cada linha da matrix. 
import numpy
import statistics

def matrix_medians(matrix: numpy.ndarray[int, int]):
    return [statistics.median(row) for row in matrix]