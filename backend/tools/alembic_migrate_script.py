import os

from manifest import load_env

def main():
    load_env()

    os.chdir(os.path.abspath(os.path.join(__file__, "..", "..")))

    os.system('alembic revision --autogenerate -m ""')
    os.system('alembic upgrade head')

if __name__ == "__main__":
    main()