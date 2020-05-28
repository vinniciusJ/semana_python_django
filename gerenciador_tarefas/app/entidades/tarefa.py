class Tarefa():
    def __index__(self, titulo, descricao, data_expiracao, prioridade):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_expiracao = data_expiracao
        self.__prioridade = prioridade

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def titulo(self, descricao):
        self.__titulo = descricao

    @property
    def data_expiracao(self):
        return self.__data_expiracao

    @data_expiracao.setter
    def titulo(self, data_expiracao):
        self.__data_expiracao = data_expiracao

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def titulo(self, prioridade):
        self.__prioridade = prioridade