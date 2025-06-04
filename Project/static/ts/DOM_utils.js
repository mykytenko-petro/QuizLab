export function createButton(args = {}) {
    const { type = "button", onclick = () => { }, textContent = "filler", } = args;
    const buttonElement = document.createElement("button");
    buttonElement.type = type;
    buttonElement.onclick = onclick;
    buttonElement.textContent = textContent;
    return buttonElement;
}
