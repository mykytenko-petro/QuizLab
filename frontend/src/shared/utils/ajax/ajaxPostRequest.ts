export function ajaxPostRequest(
    url : string,
    func : (data : object) => void,
    image? : File,
    json_data? : object
) {
    console.log("url: " + url)
    console.log("json_data: " + JSON.stringify(json_data))

    // 
    const dataToSend = new FormData()

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
            error: (error) => {console.error(error)}
        }
    )
}