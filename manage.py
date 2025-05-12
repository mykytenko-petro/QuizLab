import Project

def main():
    try:
        Project.assemble()
        Project.project.run(
            host='127.0.0.1',
            debug=True,
            port=2232
        )

    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()


print(f"Error{str(errors= Exception)}")