import subprocess

def build():
    commands_list = [
        "flask --app Project db init",
        "flask --app Project db migrate",
        "flask --app Project db upgrade"
    ]

    for command in commands_list:
        subprocess.call(args = command.split(" "))