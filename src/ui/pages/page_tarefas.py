from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QPushButton
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from typing import Literal

class TaskBox(QFrame):
    COLORS = {
            0: "#4CAF50",  # Verde para tarefas normais
            1: "#FF9800",  # Laranja para tarefas com aviso
            2: "#F44336"   # Vermelho para tarefas críticas
            }
    
    def __init__(self, titulo : str, data : str, warning : Literal[0, 1, 2]): 
        super().__init__()
        self.setObjectName("taskBox")
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("background-color: green; border-radius: 8px;")
        self.setFixedSize(600, 50)

        task_box_layout = QHBoxLayout(self)
        task_box_layout.setContentsMargins(12, 8, 12, 8)

        self.lbl_titulo = QLabel(titulo)
        self.lbl_data = QLabel(data)

        self.lbl_titulo.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.lbl_data.setFont(QFont("Arial", 10, QFont.Weight.Normal))
        self.lbl_titulo.setStyleSheet("color: white;")
        self.lbl_data.setStyleSheet(f"color: {self.COLORS[warning]};")

        task_box_layout.addWidget(self.lbl_titulo, alignment= Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        task_box_layout.addStretch()
        task_box_layout.addWidget(self.lbl_data, alignment= Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

    def mousePressEvent(self, event):
        print(f"Tarefa '{self.lbl_titulo.text()}' clicada!")
        super().mousePressEvent(event)


class TarefasPage(QWidget):
    def __init__(self):
        super().__init__()
        tarefa_page_layout = QVBoxLayout(self)

        top_bar_widget = QWidget()
        tarefa_page_layout.addWidget(top_bar_widget)

        topbar_layout = QHBoxLayout()
        top_bar_widget.setLayout(topbar_layout)

        self.btn_back = QPushButton("Voltar")
        self.btn_back.setStyleSheet("background-color: transparent; color: #4CAF50; border: none;")
        self.btn_back.setFixedSize(100, 30)
        self.btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_back.clicked.connect(lambda: print("Botão 'Voltar' clicado!"))  # Conectar o clique do botão a um método de exemplo
        topbar_layout.addWidget(self.btn_back, alignment= Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        page_name = QLabel("Tarefas")
        page_name.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        page_name.setContentsMargins(0, 0, 0, 20)
        page_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        topbar_layout.addWidget(page_name, alignment= Qt.AlignmentFlag.AlignCenter)

        self.btn_add = QPushButton("Adicionar")
        self.btn_add.setStyleSheet("background-color: transparent; color: #4CAF50; border: none;")
        self.btn_add.setFixedSize(100, 30)
        self.btn_add.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_add.clicked.connect(lambda: print("Botão 'Adicionar' clicado!"))  # Conectar o clique do botão a um método de exemplo
        topbar_layout.addWidget(self.btn_add, alignment= Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        tarefa = TaskBox("Regar as plantas", "Hoje às 18:00", warning=1)
        tarefa_page_layout.addWidget(tarefa)
        tarefa_page_layout.addStretch()