import pytest
from src import Data, Tarefa, Calendario, DeltaTime

class TestDeltaTime:
    def test_total_seconds(self):
        dt = DeltaTime(years=1, months=2, days=3, hours=4, minutes=5)
        assert dt.total_seconds() == 1*365*24*3600 + 2*30*24*3600 + 3*24*3600 + 4*3600 + 5*60

    def test_add(self):
        dt1 = DeltaTime(years=1, months=2, days=3, hours=4, minutes=5)
        dt2 = DeltaTime(years=1, months=2, days=3, hours=4, minutes=5)
        result = dt1 + dt2
        assert result.total_seconds() == 2*(1*365*24*3600 + 2*30*24*3600 + 3*24*3600 + 4*3600 + 5*60)

    def test_sub(self):
        dt1 = DeltaTime(years=1, months=2, days=3, hours=4, minutes=5)
        dt2 = DeltaTime(years=1, months=2, days=3, hours=4, minutes=5)
        result = dt1 - dt2
        assert result.total_seconds() == 0

    def test_str(self):
        dt = DeltaTime(years=1, months=2, days=3, hours=4, minutes=5)
        assert str(dt) == "1 anos, 2 meses, 3 dias, 4 horas e 5 minutos"

    def test_comparisons(self):
        dt1 = DeltaTime(years=1)
        dt2 = DeltaTime(years=2)
        assert dt1 < dt2
        assert dt2 > dt1
        assert dt1 != dt2
        assert dt1 <= dt2
        assert dt2 >= dt1
        dt3 = DeltaTime(years=1)
        assert dt1 == dt3
        assert dt1 <= dt3
        assert dt1 >= dt3

class TestData:
    def test_now(self):
        data_atual = Data.now()
        assert isinstance(data_atual, Data)
        assert (data_atual.ano, data_atual.mes, data_atual.dia) == (2026, 4, 10)

class TestTarefa:
    @pytest.mark.parametrize('nome, desc, prazo', [
        pytest.param("roberto", "samarone", 12),
        pytest.param("roberto", 12, Data(2026, 12, 2)),
        pytest.param(12, "roberto", Data(2026, 12, 2)),
    ])
    def test_init(self, nome, desc, prazo):
        with pytest.raises(TypeError):
            Tarefa(nome, desc, prazo)

    def test_tempo_restante(self):
        a = Tarefa('a', 'a', Data(2026, 4, 10, 23))
        assert a.tempo_restante < DeltaTime(days=1)

class TestCalendario:

    def test_add_tarefa(self):
        calendario = Calendario()
        calendario.add_tarefa(Tarefa("roberto", "samarone", Data(2026, 12, 2)))
        calendario.add_tarefa(Tarefa('a', 'a', Data(2026, 4, 8, 23)))
        assert calendario.lista[0] == Tarefa('a', 'a', Data(2026, 4, 8, 23))
        assert calendario.lista[1] == Tarefa("roberto", "samarone", Data(2026, 12, 2))

    def test_get_tarefa(self):
        calendario = Calendario()
        calendario.clear()
        calendario.add_tarefa(Tarefa("roberto", "samarone", Data(2026, 12, 2)))
        calendario.add_tarefa(Tarefa('a', 'a', Data(2026, 4, 8, 23)))
        assert calendario.get_tarefa(0) == Tarefa('a', 'a', Data(2026, 4, 8, 23))
        assert calendario.get_tarefa(1) == Tarefa("roberto", "samarone", Data(2026, 12, 2))

    def test_remove_tarefa(self):
        calendario = Calendario()
        calendario.clear()
        calendario.add_tarefa(Tarefa("roberto", "samarone", Data(2026, 12, 2)))
        calendario.add_tarefa(Tarefa('a', 'a', Data(2026, 4, 8, 23)))
        calendario.remover_tarefa(Tarefa('a', 'a', Data(2026, 4, 8, 23)))
        assert calendario.get_tarefa(0) == Tarefa("roberto", "samarone", Data(2026, 12, 2))

    def test_alterar_tarefa(self):
        calendario = Calendario()
        calendario.clear()
        calendario.add_tarefa(Tarefa("roberto", "samarone", Data(2026, 12, 2)))
        calendario.add_tarefa(Tarefa('a', 'a', Data(2026, 4, 8, 23)))
        calendario.alterar_tarefa(Tarefa('a', 'a', Data(2026, 4, 8, 23)), Tarefa('a', 'a', Data(2026, 12, 2)))
        assert calendario.get_tarefa(0) == Tarefa("roberto", "samarone", Data(2026, 12, 2))
        assert calendario.get_tarefa(1) == Tarefa('a', 'a', Data(2026, 12, 2))
