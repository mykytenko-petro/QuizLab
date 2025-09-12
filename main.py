def main():
    try:
        from manifest import assemble

        assemble()

        import Project

        Project.project.run(
            debug=True,
            port=2232,
            use_reloader=False
        )
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()