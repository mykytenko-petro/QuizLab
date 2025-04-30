import Project
import api
import uvicorn
import subprocess

def main():
    try:
        Project.assemble()
        
        subprocess.run(["python", "start_api.py"])
        Project.project.run(
            debug = True,
            port = 2232
        )

    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()