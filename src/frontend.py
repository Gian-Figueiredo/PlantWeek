from .application import App
from time import sleep
from threading import Thread
import subprocess
from .storage import Storage
from colorama import init, Fore, Style
init(autoreset=True)

class Tui:
    def __init__(self, controller = App()):
        self.controller = controller.facade
        self.storage = Storage()


    def exibir_menu(self):
        subprocess.run('clear', shell=True)
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\n=== Gerenciador de Tarefas ===")
        print(Fore.GREEN + Style.BRIGHT + "Menu:")
        print(Fore.GREEN + Style.BRIGHT +"1. Adicionar tarefa")
        print(Fore.GREEN + Style.BRIGHT + "2. Listar tarefas")
        print(Fore.GREEN + Style.BRIGHT + "3. Remover tarefa")
        print(Fore.GREEN + Style.BRIGHT + "4. Alterar tarefa")
        print(Fore.GREEN + Style.BRIGHT + "5. Limpar lista de tarefas")
        print(Fore.GREEN + Style.BRIGHT + "6. Salvar tarefas")
        print(Fore.GREEN + Style.BRIGHT + "0. Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            sleep(0.5)
            escolha = input("Escolha uma opção: ")
            match escolha:
                case '1':
                    self.adicionar_tarefa()
                case '2':
                    self.listar_tarefas()
                case '3':
                    self.remover_tarefa()
                case '4':
                    self.alterar_tarefa()
                case '5':
                    self.limpar_lista()
                case '6':
                    self.salvar_tarefas()
                case '0':
                    print(Fore.GREEN + Style.BRIGHT + "Saindo do programa...")
                    t = Thread(target=self.salvar_tarefas)
                    t.start()
                    t.join()
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def limpar_lista(self):
        self.controller.calendario.lista.clear()
        print(Fore.GREEN + Style.BRIGHT + "Lista de tarefas limpa com sucesso.")
        sleep(0.5)
        input("Pressione Enter para continuar...")

    def adicionar_tarefa(self):
        corretamente = False
        while not corretamente:
            subprocess.run('clear', shell=True)
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            ano = int(input("Ano do prazo: "))
            mes = int(input("Mês do prazo: "))
            dia = int(input("Dia do prazo: "))
            hora = int(input("Hora do prazo: "))
            minuto = int(input("Minuto do prazo: "))
            sleep(0.5)
            try:
                prazo = self.controller.criar_data(ano, mes, dia, hora, minuto)
                self.controller.adicionar_tarefa(nome, descricao, prazo)
            except ValueError as e:
                print(f"Erro ao adicionar tarefa: {e}")
            else:            
                print(Fore.GREEN + Style.BRIGHT + "Tarefa adicionada com sucesso.")
                corretamente = True
            finally:
                input("Pressione Enter para continuar...")

    def listar_tarefas(self):
        subprocess.run('clear', shell=True)
        tarefas = self.controller.listar_tarefas()
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            for id, tarefa in enumerate(tarefas):
                print(f"ID: {id} | Nome: {tarefa.nome} | Descrição: {tarefa.descricao} | Prazo: {tarefa.prazo}")
                sleep(0.3)
        input("Pressione Enter para continuar...")

    def salvar_tarefas(self):
        self.storage.salvar_tarefas(self.controller.listar_tarefas())
        sleep(0.5)
        print(Fore.GREEN + Style.BRIGHT + "Tarefas salvas com sucesso.")
        sleep(0.5)

    def remover_tarefa(self):
        corretamente = False
        while not corretamente:
            subprocess.run('clear', shell=True)
            id = int(input("ID da tarefa a ser removida: "))
            sleep(0.5)
            try:
                self.controller.remover_tarefa(id)
            except IndexError as e:
                print(f"Erro ao remover tarefa: {e}")
            else:
                print(Fore.GREEN + Style.BRIGHT + "Tarefa removida com sucesso.")
                corretamente = True
            finally:
                input("Pressione Enter para continuar...")

    def alterar_tarefa(self):
        subprocess.run('clear', shell=True)
        id = int(input("ID da tarefa a ser alterada: "))
        sleep(0.5)
        try:
            self.controller.remover_tarefa(id)
        except IndexError as e:
            print(f"Erro ao alterar tarefa: {e}")
            input("Pressione Enter para continuar...")
            return
        corretamento = False
        while not corretamento:
            nome = input("Novo nome da tarefa: ")
            descricao = input("Nova descrição da tarefa: ")
            ano = int(input("Ano do novo prazo: "))
            mes = int(input("Mês do novo prazo: "))
            dia = int(input("Dia do novo prazo: "))
            hora = int(input("Hora do novo prazo: "))
            minuto = int(input("Minuto do novo prazo: "))
            sleep(0.5)
            try:
                prazo = self.controller.criar_data(ano, mes, dia, hora, minuto)
                self.controller.adicionar_tarefa(nome, descricao, prazo)
            except ValueError as e:
                print(f"Erro ao alterar tarefa: {e}")
            else:
                print(Fore.GREEN + Style.BRIGHT + "Tarefa alterada com sucesso.")
                corretamento = True
            finally:
                input("Pressione Enter para continuar...")   