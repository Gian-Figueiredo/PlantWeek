from .models import Calendario, Tarefa, Data
class FacadeCalendario:
    def __init__(self):
        self.calendario = Calendario()
    
    def criar_tarefa(self, nome : str, descricao : str, prazo : Data):
        if not isinstance(prazo, Data):
            raise TypeError(f"O parâmetro prazo precisa ser do tipo Data, mas foi passado {type(prazo)}")
        return Tarefa(nome, descricao, prazo)
    
    def criar_data(self, ano : int, mes : int, dia : int, hora : int, minuto : int):
        return Data(ano, mes, dia, hora, minuto)

    def adicionar_tarefa(self, nome : str, descricao : str, prazo : Data):
        tarefa = self.criar_tarefa(nome, descricao, prazo)
        self.calendario.add_tarefa(tarefa)
    
    def remover_tarefa(self, index : int):
        if not isinstance(index, int):
            raise TypeError(f"O parâmetro index precisa ser do tipo int, mas foi passado {type(index)}")
        self.calendario.remove_tarefa(index)
    
    def listar_tarefas(self):
        return self.calendario.lista
    
class App:
    def __init__(self):
        self.facade = FacadeCalendario()