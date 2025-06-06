import Project

def main():
    try:
        Project.assemble()
        Project.project.run(
            debug=True,
            use_reloader=False,
            port=2232
        )
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()