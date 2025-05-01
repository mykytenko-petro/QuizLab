import sys
import traceback

# Import colorama for colored terminal output
from colorama import init, Fore, Style
init()  # Initialize colorama

print(Fore.GREEN + "Python version:", sys.version + Style.RESET_ALL)
print(Fore.GREEN + "Starting application..." + Style.RESET_ALL)

try:
    import Project
    print(Fore.GREEN + "Project imported successfully" + Style.RESET_ALL)
except Exception as e:
    print(Fore.RED + f"Error importing Project: {e}" + Style.RESET_ALL)
    traceback.print_exc()
    sys.exit(1)

def main():
    try:
        print(Fore.GREEN + "Building project..." + Style.RESET_ALL)
        Project.build()
        print(Fore.GREEN + "Running project..." + Style.RESET_ALL)
        Project.project.run(
            debug=True,
            port=2232
        )
    except Exception as error:
        print(Fore.RED + f"Error running project: {error}" + Style.RESET_ALL)
        traceback.print_exc()

if __name__ == '__main__':
    main()
