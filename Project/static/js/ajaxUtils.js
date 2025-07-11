export function ajaxGetRequest(url, func) {
    console.log("url: " + url)
    // console.log("func: " + func)

    $.ajax(
        {
            url: url,
            method: 'GET',
            success: (data) => {
                console.log(data)
                func(data)
            },
            error: (error) => {console.log(error)}
        }
    )
}

export function ajaxPostRequest(url, func, image, json_data) {
    console.log("url: " + url)
    // console.log("func: " + func)
    console.log("image: " + image)
    console.log("json_data: " + JSON.stringify(json_data))

    // 
    let dataToSend = new FormData()

    // 
    if (json_data) {
        dataToSend.append("data", JSON.stringify(json_data))
    } else {
        dataToSend.append("data", JSON.stringify({}))
    }
    
    if (image) {
        dataToSend.append("image", image)
    }

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