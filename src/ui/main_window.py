from PyQt6.QtWidgets import (
    QMainWindow, QHBoxLayout, QWidget, QLabel, QVBoxLayout,
    QPushButton, QStackedWidget
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from .pages.page_tarefas import TarefasPage

STYLE_BUTTON = "background-color: #4CAF50; color: white; border: none; padding: 10px;"

class PlaceholderWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        layout = QVBoxLayout()
        page_name = QLabel(text)
        page_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(page_name, alignment= Qt.AlignmentFlag.AlignBottom)
        warning = QLabel("Está página ainda está em desenvolvimento.")
        warning.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        warning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(warning, alignment= Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setar configurações da janela
        self.setWindowTitle("Gerenciador de Tarefas")
        self.setGeometry(100, 100, 800, 600)


        # ===== LAYOUT PRINCIPAL =====
        # widget central
        # widget que irá cobrir toda a janela, para que possamos colocar outros widgets dentro dele
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layout principal
        # layout que irá organizar os widgets dentro do widget central
        # Colocaremos horizontalmente, para que possamos colocar a barra lateral e o conteúdo principal lado a lado
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # ===== BARRA LATERAL =====
        # widget da barra lateral
        sidebar_widget = QWidget()
        sidebar_widget.setFixedWidth(250)
        main_layout.addWidget(sidebar_widget)

        # layout da barra lateral
        sidebar_layout = QVBoxLayout()
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(10)

        # Nome do App
        app_label = QLabel("PlantWeek")
        app_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        app_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        app_label.setStyleSheet("color: #4CAF50;")  # Cor verde para o nome do app
        app_label.setFixedHeight(50)
        app_label.setContentsMargins(0, 0, 0, 0)  # Margem inferior para separar do resto dos botões
        sidebar_layout.addWidget(app_label)

        # Botões da barra lateral
        self.btn_tarefas = QPushButton("Tarefas")
        self.btn_configuracoes = QPushButton("Configurações")
        self.btn_manual = QPushButton("Manual do Usuário")
        self.btn_sobre = QPushButton("Sobre")

        self.btn_tarefas.setStyleSheet(STYLE_BUTTON)
        self.btn_configuracoes.setStyleSheet(STYLE_BUTTON)
        self.btn_manual.setStyleSheet(STYLE_BUTTON)
        self.btn_sobre.setStyleSheet(STYLE_BUTTON)

        # Stack para trocar entre as páginas
        self.stack = QStackedWidget()  

        self.page_tarefa = TarefasPage()  # Página de Tarefas
        self.page_config = PlaceholderWidget("Página de Configurações")
        self.page_manual = PlaceholderWidget("Página do Manual do Usuário")
        self.page_sobre = PlaceholderWidget("Página Sobre")

        self.stack.addWidget(self.page_tarefa)  # Página de Tarefas
        self.stack.addWidget(self.page_config)  # Página de Configurações
        self.stack.addWidget(self.page_manual)  # Página do Manual do Usuário
        self.stack.addWidget(self.page_sobre)  # Página Sobre

        # Conectar os botões para trocar as páginas
        self.btn_tarefas.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_configuracoes.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_manual.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.btn_sobre.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        # Adicionar os botões à barra lateral
        sidebar_layout.addWidget(self.btn_tarefas)
        sidebar_layout.addWidget(self.btn_configuracoes)
        sidebar_layout.addWidget(self.btn_manual)
        sidebar_layout.addWidget(self.btn_sobre, alignment=Qt.AlignmentFlag.AlignTop)

        self.stack.setCurrentIndex(0)  # Mostrar a página de tarefas por padrão

        # ===== CONTEÚDO PRINCIPAL =====
        # widget do conteúdo principal
        main_layout.addWidget(self.stack, 1) # O "1" indica que o stack deve ocupar o espaço restante da janela, enquanto a barra lateral tem largura fixa



