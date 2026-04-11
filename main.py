if __name__ == "__main__":
    from src import Tui
    app = Tui()
    app.storage.carregar_bd(app.controller.calendario)
    app.executar()