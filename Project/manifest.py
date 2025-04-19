import os

def assemble():
    if not os.path.exists(os.path.abspath(os.path.join(__file__, '..', "migrations"))):
        os.system(os.environ["DB_INIT"])
    
    os.system(os.environ["DB_MIGRATE"])
    os.system(os.environ["DB_UPGRADE"])