import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from manifest import load_env


def main():
    load_env()

    os.system('alembic revision --autogenerate -m ""')
    os.system('alembic upgrade head')

if __name__ == "__main__":
    main()