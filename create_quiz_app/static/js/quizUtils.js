export function ajaxPostRequest(data, func) {
    $.ajax(
        {
            url: '/create_quiz_api',
            method: 'POST',
            processData: false,
            contentType: false,
            data: data,
            success: (data) => {
                console.log(data)
                func(data)
            },
            error: (error) => {console.log(error)}
        }
    )
}