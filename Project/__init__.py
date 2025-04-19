

# Then import settings (which initializes the app)
from .settings import project

# Import these modules after the app is initialized
from .manifest import build
from .urls import *
from .core import *

# Import login manager last
from .login_manager import load_user, login_manager



#from .database import DATABASE
#from .settings import project
#
## Initialize the database and app
#project.secret_key = "SECRET_KEY123"
#
## Import registration_app AFTER database is initialized
#import registration_app
#import home_app
#
## Now import login manager AFTER the registration_app is imported
#from .login_manager import load_user, login_manager
#from .manifest import build
#from .urls import *
#from .core import *