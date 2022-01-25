#Modules:

import numpy as np

#Public:

class DataLoader:
    '''
    Classe responsável por gerenciar a padronização das entradas
    das enquentes parciais.
    '''

    #Constructor

    def __init__(
        self,
        fonte,
        paredao
    ):

        self._fonte = fonte

        self._paredao_names = paredao.get_participantes()

        self._content = []

    #Interface

    def set_manual_entries(
        self,
        num_participante_1,
        num_participante_2,
        num_participante_3
    ):
        '''
        Define as entradas de forma manual.
        '''

        for _ in range(0, num_participante_1):

            self._content.append(
                self._new_data_entry(
                    is_participante_1 = True
                )
            )

        for _ in range(0, num_participante_2):

            self._content.append(
                self._new_data_entry(
                    is_participante_2 = True
                )
            )

        for _ in range(0, num_participante_3):

            self._content.append(
                self._new_data_entry(
                    is_participante_3 = True
                )
            )

    def get(self, max_samples = 0):
        '''
        Retorna os dados de uma fonte. Sendo possível definir um
        número limite de amostras.
        '''

        if max_samples:

            return list(np.random.choice(self._content, max_samples))

        else:

            return self._content 

    #Implementation

    def _new_data_entry(
        self,
        is_participante_1 = False,
        is_participante_2 = False,
        is_participante_3 = False
    ):

        return {
            self._paredao_names[0] : is_participante_1,
            self._paredao_names[1] : is_participante_2,
            self._paredao_names[2] : is_participante_3,
            'Fonte' : self._fonte
        }

           
