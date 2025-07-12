import { ElementProperties } from "./types"

interface FormProperties extends ElementProperties {
    method?: "get" | "post"
    enctype?: "multipart/form-data"
}

export function createFormElement(props: FormProperties = {}) {
    const {
        id,
        className,
        method = "post",
        enctype = "multipart/form-data"
    } = props

    const formElement = document.createElement("form")

    if (id) formElement.id = id
    if (className) formElement.className = className

    formElement.method = method
    formElement.enctype = enctype

    return formElement
}
