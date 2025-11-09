import os

def build_app():
    os.system("pyinstaller --name kaibi_todo -F main.py")

build_app()