#Public:

class Paredao:
    '''
    Representa o paredão e os seus participantes
    '''

    #Constructor

    def __init__(
        self,
        participante_1,
        participante_2,
        participante_3,
    ):

        self._participante_1 = participante_1

        self._participante_2 = participante_2

        self._participante_3 = participante_3

    #Interface

    def get_participantes(self):
        '''
        Retorna uma lista com o nome dos participantes no paredão
        '''

        return [
            self._participante_1,
            self._participante_2,
            self._participante_3,
        ]