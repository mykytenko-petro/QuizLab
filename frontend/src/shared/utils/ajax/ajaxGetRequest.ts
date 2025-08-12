// import { redirectInApp } from "../general"

export function ajaxGetRequest(
    url : string,
    func? : (data : object) => null
): void | string | object {
    console.log("url: " + url)

    $.ajax(
        {
            url: url,
            method: 'GET',
            success: (data) => {
                if (func) {
                    func(data)
                } else {
                    if (data.redirect) {
                        console.log("making redirect to: " + data.redirect)
                        // redirectInApp(data.redirect)

                        return
                    }

                    console.log(data)
                    return data
                }
            },
            error: (error) => {console.error(error)}
        }
    )
}