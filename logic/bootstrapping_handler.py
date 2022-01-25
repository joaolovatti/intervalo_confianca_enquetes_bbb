#Modules:

import pandas as pd

#Public:

class BootstrappingHandler:
    '''
    Executa um bootstrapping nas amostras.
    '''

    #Constructor

    def __init__(self):

        self._samples_mean = []

        self._interactions = 10_000

    #Interface

    def from_data_frame(self, df, column_name, sample_size):
        '''
        Executa um bootstrapping numa coluna de um DataFrame
        '''

        for _ in range(0, self._interactions):

            sample_mean = df.sample(sample_size, replace = True)[column_name].mean()

            self._samples_mean.append(sample_mean)

    def get_samples(self):

        return self._samples_mean