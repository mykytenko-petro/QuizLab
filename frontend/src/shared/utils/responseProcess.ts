import type { IResponseProcess } from "../types";


export function responseProcess({ response }: IResponseProcess) {
    try {
        if ("redirect" in response) {
            console.log("redirect on" + response.redirect)

            window.location.replace(response.redirect as string)

            return null
        } else {
            return response
        }
    } catch {
        return response
    }
}