import { ElementProperties } from "./types"

interface ButtonProperties extends ElementProperties {
    func : () => void
    textContent? : string
    type? : "button"
}

export function createButtonElement(props: ButtonProperties) {
    const {
        id,
        className,
        func,
        textContent,
        type = "button"
    } = props

    const buttonElement = document.createElement("button")

    if (id) buttonElement.id = id
    if (className) buttonElement.className = className

    buttonElement.type = type

    if (type === "button") {
        buttonElement.addEventListener("click", func)
    }

    if (textContent) buttonElement.textContent = textContent

    return buttonElement
}