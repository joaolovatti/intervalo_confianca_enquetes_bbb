
#Public:

class EnqueteDataList:
    '''
    Classe responsável por representar uma lista de dados que contém
    todas as entradas das enquetes parciais.
    '''

    #Constructor
    
    def __init__(self):
        
        self._content = []
        
    #Interface

    def append(self, new_list):
        '''
        Anexa todos os valores de uma lista.
        '''
        
        for item in new_list:
            
            self._content.append(item)

    def get(self):

        return self._content