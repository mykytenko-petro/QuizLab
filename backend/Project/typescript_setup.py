import flask


typescriptManagerApp = flask.Blueprint(
    name="ts",
    import_name="Project",
    static_folder="dist",
    static_url_path="/js"
)