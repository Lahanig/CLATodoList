import os

def build_app():
    os.system("pyinstaller --name CLATodoList -F main.py")

build_app()
