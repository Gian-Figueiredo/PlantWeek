from datetime import datetime
from .utils import type_check

class DeltaTime:
    def __init__(self, years : int = 0, months: int = 0, days: int = 0, hours: int = 0, minutes: int = 0):
        type_check(years, months, days, hours, minutes, expected_type=int)
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def total_seconds(self):
        return (self.years * 31536000) + (self.months * 2592000) + (self.days * 86400) + (self.hours * 3600) + (self.minutes * 60)

    def __lt__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return self.total_seconds() < other.total_seconds()
    
    def __gt__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return self.total_seconds() > other.total_seconds()
    
    def __eq__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return self.total_seconds() == other.total_seconds()
    
    def __le__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return self < other or self == other
    
    def __ge__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return self > other or self == other
    
    def __ne__(self, value):
        if not isinstance(value, DeltaTime):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(value)}")
        return not self == value
    
    def __add__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Adição entre tipos incompatíveis: {type(self)} e {type(other)}")
        total_seconds = self.total_seconds() + other.total_seconds()
        years, remainder = divmod(total_seconds, 31536000)
        months, remainder = divmod(remainder, 2592000)
        days, remainder = divmod(remainder, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, _ = divmod(remainder, 60)
        return DeltaTime(years=int(years), months=int(months), days=int(days), hours=int(hours), minutes=int(minutes))
    
    def __sub__(self, other):
        if not isinstance(other, DeltaTime):
            raise TypeError(f"Subtração entre tipos incompatíveis: {type(self)} e {type(other)}")
        total_seconds = other.total_seconds() - self.total_seconds()
        years, remainder = divmod(total_seconds, 31536000)
        months, remainder = divmod(remainder, 2592000)
        days, remainder = divmod(remainder, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, _ = divmod(remainder, 60)
        return DeltaTime(years=int(years), months=int(months), days=int(days), hours=int(hours), minutes=int(minutes))

    def __str__(self):
        parts = []
        if self.years:
            parts.append(f"{self.years} anos")
        if self.months:
            parts.append(f"{self.months} meses")
        if self.days:
            parts.append(f"{self.days} dias")
        if self.hours:
            parts.append(f"{self.hours} horas")
        if self.minutes:
            parts.append(f"{self.minutes} minutos")
        return ", ".join(parts[:-1]) + " e " + parts[-1] if len(parts) > 1 else parts[0] if parts else "0 minutos"

class Data:
    def __init__(self, ano : int, mes : int, dia : int, hora : int = 0, minuto : int = 0):
        type_check(ano, mes, dia, hora, minuto, expected_type=int)
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto

    @classmethod
    def now(cls):
        return cls.fromtimestamp(datetime.now().timestamp())
    
    @classmethod
    def fromtimestamp(cls, timestamp):
        dt = datetime.fromtimestamp(timestamp)
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute)
    
    def __sub__(self, other):
        if not isinstance(other, Data):
            raise TypeError(f"Subtração entre tipos incompatíveis: {type(self)} e {type(other)}")
        dt1 = DeltaTime(years=self.ano, months=self.mes, days=self.dia, hours=self.hora, minutes=self.minuto)
        dt2 = DeltaTime(years=other.ano, months=other.mes, days=other.dia, hours=other.hora, minutes=other.minuto)
        return dt1 - dt2
    
    def __lt__(self, other):
        if not isinstance(other, Data):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return (self.ano, self.mes, self.dia, self.hora, self.minuto) < (other.ano, other.mes, other.dia, other.hora, other.minuto)
    
    def __gt__(self, value):
        if not isinstance(value, Data):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(value)}")
        return (self.ano, self.mes, self.dia, self.hora, self.minuto) > (value.ano, value.mes, value.dia, value.hora, value.minuto)
    
    def __eq__(self, other):
        if not isinstance(other, Data):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return (self.ano, self.mes, self.dia, self.hora, self.minuto) == (other.ano, other.mes, other.dia, other.hora, other.minuto)
    
    def __le__(self, other):
        if not isinstance(other, Data):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return self < other or self == other
    
    def __ge__(self, value):
        if not isinstance(value, Data):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(value)}")
        return self > value or self == value
    
    def __ne__(self, value):
        if not isinstance(value, Data):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(value)}")
        return not self == value
    
    def __str__(self):
        return f"{self.ano:04d}-{self.mes:02d}-{self.dia:02d} {self.hora:02d}:{self.minuto:02d}"

class Tarefa:
    def __init__(self, nome : str, descricao : str, prazo : Data):
        if not (isinstance(nome, str) and isinstance(descricao, str) and isinstance(prazo, Data)):
            raise TypeError(f"Os parâmetros (nome, descricao, prazo) precisam ser (str, str, Data), mas foi passado {(type(nome), type(descricao), type(prazo))}")
        self.nome = nome
        self.descricao = descricao
        self.prazo = prazo

    @property
    def tempo_restante(self):
        return Data.now() - self.prazo
    
    def __str__(self):
        return f"Tarefa: {self.nome}, Descrição: {self.descricao}, Prazo: {self.prazo}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Tarefa):
            raise TypeError(f"Comparação entre tipos incompatíveis: {type(self)} e {type(other)}")
        return (self.nome, self.descricao, self.prazo) == (other.nome, other.descricao, other.prazo)
    
class Calendario:
    def __init__(self, iteravel = list[Tarefa]()):
        self.lista : list[Tarefa] = iteravel

    def add_tarefa(self, tarefa : Tarefa):
        self.lista.append(tarefa)
        self.lista.sort(key=lambda tarefa : tarefa.prazo)

    def get_tarefa(self, index : int):
        return self.lista[index]

    def remover_tarefa(self, tarefa : Tarefa):
        self.lista.remove(tarefa)

    def alterar_tarefa(self, antiga_tarefa : Tarefa, nova_tarefa : Tarefa):
        self.remover_tarefa(antiga_tarefa)
        self.add_tarefa(nova_tarefa)

    def __repr__(self):
        return f"Calendário com {len(self.lista)} tarefas: {self.lista}"
    
    def __str__(self):
        return self.__repr__()
    
    def clear(self):
        self.lista.clear()