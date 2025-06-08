interface TagArguments {
    name?: string
    textContent?: string
    onclick?: () => void
    type?: "button" | "submit"
}

export function createButton(args: TagArguments = {}) {
    const {
        type = "button",
        onclick = () => {},
        textContent = "filler",
    } = args

    const buttonElement = document.createElement("button");

    buttonElement.type = type;
    buttonElement.onclick = onclick;
    buttonElement.textContent = textContent;

    return buttonElement;
}
