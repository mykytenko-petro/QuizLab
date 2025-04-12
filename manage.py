import Project

def main():
    try:
        print("path:", Project.settings.path)
        Project.project.run(
            debug = True,
            port = 2232
        )

    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()