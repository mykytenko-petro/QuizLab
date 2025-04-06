import Project

def main():
    try:
        Project.project.run(port = 8000)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()