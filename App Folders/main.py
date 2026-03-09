import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class AppFolder(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.setAcceptDrops(True) # THIS ENABLES DRAG & DROP
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Drag shortcuts here to add them")
        self.layout.addWidget(self.label)
        
        # Load existing apps from the file
        with open(self.file_path, "r") as f:
            for line in f:
                btn = QPushButton(line.strip().split('\\')[-1])
                btn.clicked.connect(lambda ch, p=line.strip(): self.launch(p))
                self.layout.addWidget(btn)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 200, 400)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        with open(self.file_path, "a") as f:
            for f_path in files:
                f.write(f_path + "\n")
        self.initUI() # Refresh the list

    def launch(self, path):
        import os
        os.startfile(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # The %1 from the registry becomes sys.argv[1]
    ex = AppFolder(sys.argv[1])
    ex.show()
    sys.exit(app.exec())