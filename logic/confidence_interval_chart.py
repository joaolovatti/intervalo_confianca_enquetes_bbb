#Modules:

import matplotlib.pyplot as plt

import numpy as np

#Public

class ConfidenceIntervalChart:
    '''
    Chart padronizada para ilustrar um intervalo de confiança
    '''

    #Constructor

    def __init__(self, values, interval, name):

        self._values = values

        self._interval = interval

        self._name = name

    #Interface

    def plot(self):

        lower_bound = np.percentile(self._values, (100 - self._interval) / 2)

        upper_bound = np.percentile(self._values, 100 - (100 - self._interval) / 2)
    
        plt.figure(figsize = (8.5, 6))
    
        plt.hist(self._values);

        plt.title(f'Distribuição da média - {self._name}');

        plt.ylabel('Frequência');

        plt.xlabel('Média da amostra');

        plt.axvline(lower_bound, color = 'orange');

        plt.axvline(upper_bound, color = 'red');

        plt.legend(
            [f'{(lower_bound * 100):1.2f}%', f'{(upper_bound * 100):1.2f}%'], 
            title = f'Intervalo de confinaça de {self._interval}%'
        );

        plt.show()