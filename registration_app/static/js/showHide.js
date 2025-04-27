function showHide(id) {
    button = document.querySelector(`#${id}`)

    if (button.type === "password") {
        button.type = "text"
        button.text = "🙉"
    } else {
        button.type = "password"
        button.text = "🙈"
    }
}