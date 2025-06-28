export function getSlug() {
    return window.location.href.split("/").pop()
}

export function redirectInApp(url) {
    window.location.replace(`${url}`)
}

export function ajaxPostRequest(url, json_data, func, image) {
    console.log("url: " + url)
    console.log("json_data: " + json_data)
    console.log("func: " + func)
    console.log("image: " + image)

    // 
    let dataToSend = new FormData()

    // 
    dataToSend.append("data", JSON.stringify(json_data))
    dataToSend.append("image", image)

    // 
    $.ajax(
        {
            url: url,
            method: 'POST',
            processData: false,
            contentType: false,
            data: dataToSend,
            success: (data) => {
                console.log(data)
                func(data)
            },
            error: (error) => {console.log(error)}
        }
    )
}