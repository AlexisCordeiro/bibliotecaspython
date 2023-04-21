#5° Scipy, biblioteca muito usada para trabalhar com matemática e estatística
from scipy import stats

data = [1, 2, 3, 4, 5]

median = stats.median(data)
mode = stats.mode(data)

print('A mediana dos dados é:', median)
print('A moda dos dados é:', mode.mode[0])