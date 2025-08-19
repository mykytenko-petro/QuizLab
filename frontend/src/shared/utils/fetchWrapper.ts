import type { IFetchWrapper } from "../types";

export async function fetchWrapper(props : IFetchWrapper) : Promise<void> {
    try {
        const response = await fetch(
            props.url,
            {
                method: "POST",
                body: props.body
            }
        )
        const data = await response.json();
        props.func(data)
        
    } catch (error) {
        console.log("error has occurred:\n" + error)
    }
}