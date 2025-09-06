export function ajaxGetRequest(
    url : string,
    func : (data : object) => void
) {
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
            error: (error) => {console.error(error)}
        }
    )
}