import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))

import asyncio

from manifest import load_env


def main():
    load_env()

    from Project.database import create_db_and_tables

    asyncio.run(create_db_and_tables())

if __name__ == "__main__":
    main()