export function createButtonElement(func, textContent, type = "button") {
    const buttonElement = document.createElement("button")

    buttonElement.type = type
    buttonElement.onclick = () => { func() }
    buttonElement.textContent = textContent

    return buttonElement
}