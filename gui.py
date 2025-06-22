from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QListWidget, QComboBox,
                             QFileDialog, QMessageBox, QGridLayout)
from PyQt6.QtGui import QPixmap
from auth import register, login
from database import init_db, add_category, add_brand, add_product, get_categories, get_brands, get_products
import sys
from PIL import Image
import os

class TiendaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tienda Virtual - PyQt6")
        self.setGeometry(100, 100, 600, 400)
        init_db()
        self.current_user = None
        self.show_login()

    def show_login(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Iniciar Sesión"))
        layout.addWidget(QLabel("Email:"))
        self.email_entry = QLineEdit()
        layout.addWidget(self.email_entry)
        layout.addWidget(QLabel("Contraseña:"))
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_entry)
        login_button = QPushButton("Iniciar Sesión")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)
        register_button = QPushButton("Ir a Registro")
        register_button.clicked.connect(self.show_register)
        layout.addWidget(register_button)
        self.central_widget.setLayout(layout)

    def show_register(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Registrarse"))
        layout.addWidget(QLabel("Nombre de usuario:"))
        self.username_entry = QLineEdit()
        layout.addWidget(self.username_entry)
        layout.addWidget(QLabel("Email:"))
        self.email_entry = QLineEdit()
        layout.addWidget(self.email_entry)
        layout.addWidget(QLabel("Contraseña:"))
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_entry)
        register_button = QPushButton("Registrarse")
        register_button.clicked.connect(self.handle_register)
        layout.addWidget(register_button)
        back_button = QPushButton("Volver a Login")
        back_button.clicked.connect(self.show_login)
        layout.addWidget(back_button)
        self.central_widget.setLayout(layout)

    def handle_register(self):
        username = self.username_entry.text()
        email = self.email_entry.text()
        password = self.password_entry.text()
        success, message = register(username, email, password)
        QMessageBox.information(self, "Resultado", message)
        if success:
            self.show_login()

    def handle_login(self):
        email = self.email_entry.text()
        password = self.password_entry.text()
        success, message = login(email, password)
        QMessageBox.information(self, "Resultado", message)
        if success:
            self.current_user = email
            self.show_main_menu()

    def show_main_menu(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Bienvenido, {self.current_user}"))
        layout.addWidget(QPushButton("Gestionar Categorías", clicked=self.show_categories))
        layout.addWidget(QPushButton("Gestionar Marcas", clicked=self.show_brands))
        layout.addWidget(QPushButton("Gestionar Productos", clicked=self.show_products))
        layout.addWidget(QPushButton("Cerrar Sesión", clicked=self.show_login))
        self.central_widget.setLayout(layout)

    def show_categories(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestión de Categorías"))
        layout.addWidget(QLabel("Nombre de la categoría:"))
        self.category_entry = QLineEdit()
        layout.addWidget(self.category_entry)
        add_button = QPushButton("Agregar Categoría")
        add_button.clicked.connect(self.add_category)
        layout.addWidget(add_button)
        layout.addWidget(QLabel("Categorías existentes:"))
        self.category_list = QListWidget()
        layout.addWidget(self.category_list)
        self.update_category_list()
        back_button = QPushButton("Volver")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)
        self.central_widget.setLayout(layout)

    def add_category(self):
        name = self.category_entry.text()
        if name:
            add_category(name)
            self.category_entry.clear()
            self.update_category_list()
            QMessageBox.information(self, "Éxito", "Categoría agregada")

    def update_category_list(self):
        self.category_list.clear()
        for cat_id, name in get_categories():
            self.category_list.addItem(f"{cat_id}: {name}")

    def show_brands(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestión de Marcas"))
        layout.addWidget(QLabel("Nombre de la marca:"))
        self.brand_entry = QLineEdit()
        layout.addWidget(self.brand_entry)
        add_button = QPushButton("Agregar Marca")
        add_button.clicked.connect(self.add_brand)
        layout.addWidget(add_button)
        layout.addWidget(QLabel("Marcas existentes:"))
        self.brand_list = QListWidget()
        layout.addWidget(self.brand_list)
        self.update_brand_list()
        back_button = QPushButton("Volver")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)
        self.central_widget.setLayout(layout)

    def add_brand(self):
        name = self.brand_entry.text()
        if name:
            add_brand(name)
            self.brand_entry.clear()
            self.update_brand_list()
            QMessageBox.information(self, "Éxito", "Marca agregada")

    def update_brand_list(self):
        self.brand_list.clear()
        for brand_id, name in get_brands():
            self.brand_list.addItem(f"{brand_id}: {name}")

    def show_products(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QGridLayout()

        layout.addWidget(QLabel("Gestión de Productos"), 0, 0, 1, 2)
        layout.addWidget(QLabel("Nombre del producto:"), 1, 0)
        self.product_entry = QLineEdit()
        layout.addWidget(self.product_entry, 1, 1)
        layout.addWidget(QLabel("Categoría:"), 2, 0)
        self.category_combo = QComboBox()
        layout.addWidget(self.category_combo, 2, 1)
        layout.addWidget(QLabel("Marca:"), 3, 0)
        self.brand_combo = QComboBox()
        layout.addWidget(self.brand_combo, 3, 1)
        layout.addWidget(QLabel("Foto:"), 4, 0)
        self.photo_path = ""
        self.photo_label = QLabel("No seleccionada")
        layout.addWidget(self.photo_label, 4, 1)
        select_photo_button = QPushButton("Seleccionar Foto")
        select_photo_button.clicked.connect(self.select_photo)
        layout.addWidget(select_photo_button, 5, 0)
        add_button = QPushButton("Agregar Producto")
        add_button.clicked.connect(self.add_product)
        layout.addWidget(add_button, 5, 1)
        layout.addWidget(QLabel("Productos existentes:"), 6, 0, 1, 2)
        self.product_list = QListWidget()
        self.product_list.itemClicked.connect(self.show_product_image)
        layout.addWidget(self.product_list, 7, 0, 1, 2)
        self.image_label = QLabel()
        layout.addWidget(self.image_label, 7, 2)
        back_button = QPushButton("Volver")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button, 8, 0, 1, 2)
        self.update_product_list()
        self.central_widget.setLayout(layout)

    def select_photo(self):
        path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Foto", "", "Images (*.png *.jpg *.jpeg)")
        if path:
            self.photo_path = path
            self.photo_label.setText(os.path.basename(path))

    def add_product(self):
        name = self.product_entry.text()
        category = self.category_combo.currentText()
        brand = self.brand_combo.currentText()
        if name and category and brand and self.photo_path:
            category_id = category.split(":")[0]
            brand_id = brand.split(":")[0]
            add_product(name, category_id, brand_id, self.photo_path)
            self.product_entry.clear()
            self.category_combo.setCurrentIndex(0)
            self.brand_combo.setCurrentIndex(0)
            self.photo_path = ""
            self.photo_label.setText("No seleccionada")
            self.update_product_list()
            QMessageBox.information(self, "Éxito", "Producto agregado")
        else:
            QMessageBox.warning(self, "Error", "Completa todos los campos")

    def update_product_list(self):
        self.product_list.clear()
        self.category_combo.clear()
        self.brand_combo.clear()
        for cat_id, name in get_categories():
            self.category_combo.addItem(f"{cat_id}: {name}")
        for brand_id, name in get_brands():
            self.brand_combo.addItem(f"{brand_id}: {name}")
        for prod_id, name, cat, brand, photo in get_products():
            self.product_list.addItem(f"{prod_id}: {name} ({cat}, {brand})")

    def show_product_image(self, item):
        index = self.product_list.row(item)
        product = get_products()[index]
        photo_path = product[4]
        if photo_path:
            pixmap = QPixmap(photo_path)
            pixmap = pixmap.scaled(100, 100)
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TiendaApp()
    window.show()
    sys.exit(app.exec())