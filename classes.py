class Classes:

    def __init__(self, nome, atr_conjuracao, id=None):
        self.nome = nome
        self.atr_conjuracao = atr_conjuracao
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_atr_conjuracao(self):
        return self.atr_conjuracao

    def set_atr_conjuracao(self, atr_conjuracao):
        self.atr_conjuracao = atr_conjuracao

    def __str__(self):
        return f"Nome: {self.nome} \n" \
            f"Atributo de Conjuração: {self.atr_conjuracao}"


class Armaduras:

    def __init__(self, nome, defesa, tipo, id=None):
        self.nome = nome
        self.defesa = defesa
        self.tipo = tipo
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_defesa(self):
        return self.defesa

    def set_defesa(self, defesa):
        self.defesa = defesa

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Nome: {self.nome} \n" \
            f"Defesa: {self.defesa} \n" \
            f"Tipo: {self.tipo}"


class Armas:

    def __init__(self, nome, propriedade, tipo, id=None):
        self.nome = nome
        self.propriedade = propriedade
        self.tipo = tipo
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_propriedade(self):
        return self.propriedade

    def set_propriedade(self, defesa):
        self.propriedade = propriedade

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Nome: {self.nome} \n" \
            f"Propriedade: {self.propriedade} \n" \
            f"Tipo: {self.tipo}"


class Magias:

    def __init__(self, nome, nivel, alcance, id=None):
        self.nome = nome
        self.nivel = nivel
        self.alcance = alcance
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        self.nivel = nivel

    def get_alcance(self):
        return self.alcance

    def set_alcance(self, alcance):
        self.alcance = alcance

    def __str__(self):
        return f"Nome: {self.nome} \n" \
            f"Nível: {self.nivel} \n" \
            f"Alcance: {self.alcance}"
