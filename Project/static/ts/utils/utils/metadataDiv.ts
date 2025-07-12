export class MetadataDiv {
    div : HTMLDivElement

    constructor(div : HTMLDivElement, metadata? : object) {
        if (!div) {
            this.div = document.createElement("div")
        } else {
            this.div = div
        }

        if (metadata) {
            this.setAttributes(metadata)
        }
    }

    setAttributes(metadata : object) {
        for (const key in metadata) {
            this.div.dataset[key] = String(metadata[key])
        }
    }

    getAttribute(key : string): string | number | boolean {
        const value = this.div.dataset[key]

        if (value === "true") return true
        if (value === "false") return false

        if (value === "") return ""

        const num = Number(value)

        if (isNaN(num)) {
            return value
        } else {
            return num
        }
    }

    replaceChildren() {
        this.div.replaceChildren()
    }

    // ...nodes is like *nodes in python (multiple arguments)
    append(...nodes: Array<Node>) {
        this.div.append(...nodes)
    }

    querySelector<E extends Element = Element>(selectors: string): E | null {
        return this.div.querySelector(selectors)
    }
}