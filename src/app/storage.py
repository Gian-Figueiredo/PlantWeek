import json, os
from .models import Tarefa, Data, Calendario
PATH = os.path.expanduser("~/Desktop/projetos/PlantWeek/database/tarefas.json")

class Storage:
    def __init__(self):
        self.data = {}

    def salvar_tarefas(self, tarefas : list[Tarefa]):
        with open(PATH, 'w') as f:
            json.dump([parse_Tarefa(tarefa) for tarefa in tarefas], f, indent=4)

    def load_tarefas(self):
        try:
            with open(PATH, 'r') as f:
                return [load_Tarefa(tarefa_tuple) for tarefa_tuple in json.load(f)]
        except FileNotFoundError:
            os.makedirs(os.path.dirname(PATH), exist_ok=True)
            return []
        
    def carregar_bd(self, bd : Calendario):
        tarefas = self.load_tarefas()
        for tarefa in tarefas:
            bd.add_tarefa(tarefa)

def parse_Data(data : Data) -> tuple[int, int, int, int, int]:
    return (data.ano, data.mes, data.dia, data.hora, data.minuto)
  
def parse_Tarefa(tarefa : Tarefa) -> tuple[str, str, tuple[int, int, int, int, int]]:
    return (tarefa.nome, tarefa.descricao, parse_Data(tarefa.prazo))

def load_Data(data_tuple : tuple[int, int, int, int, int]) -> Data:
    return Data(*data_tuple)

def load_Tarefa(tarefa_tuple : tuple[str, str, tuple[int, int, int, int, int]]) -> Tarefa:
    nome, descricao, prazo_tuple = tarefa_tuple
    prazo = load_Data(prazo_tuple)
    return Tarefa(nome, descricao, prazo)
