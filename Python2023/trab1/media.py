#media
# Alexandre(1.9), Alisson(1.68), Ana, Antonia(1.7), Bruno h(1.93), Bruno m(1.73), Caroline(1.67), Cristian, Eduardo, Gabriel(1.75), George, Matias(1.8), Paulo(1.63), Sergio(1.81), Victor, Vinicius(1.7)
import statistics
#1.73, 1.81, 1.63, 1.80, 1.9, 1.73, 1.7, 0.2, 1.7, 1.93, 1.75, 1.78, 1.68, 1.7, 1.67
from statistics import mean
 
if __name__ == '__main__':

    #lista com as alturas
    alt = [1.73, 1.81, 1.63, 1.80, 1.9, 1.73, 1.7, 0.2, 1.7, 1.93, 1.75, 1.78, 1.68, 1.7, 1.67]
    alt2 = [1.73, 1.81, 1.63, 1.80, 1.9, 1.73, 1.7, 1.7, 1.93, 1.75, 1.78, 1.68, 1.7, 1.67]
    #Lista de alunos e altura
    alu = [{"Alexandre":'1.9', "Alisson":'1.68', "Ana":'', "Antonia":'1.7', "Bruno H":'1.93', "Bruno M":'1.73', "Caroline":'1.67', "Cristian":'', "Eduardo":'', "Gabriel":'1.75', "George":'', "Matias":'1.8', "Paulo":'1.63', "Sergio":'1.81', "Victor":'', "Vinicius":'1.7'}]
    alu2 = alu[]
    #mean e uma biblioteca que calcula a media
    avg = mean(alt)
    #imprime a media
    print(alu)
    print(avg)        # 3.0


    #Variancia
    variC = statistics.variance(alt)
    variS = statistics.variance(alt2)
    print("A variancia com gnomo: ", variC, " variancia sem gnomo: ", variS)

    #D
    desv = statistics.stdev(alt)
    desvS = statistics.stdev(alt2)
    print("O desvio padrão com gnomo: ", desv, " sem gnomo: ", desvS)