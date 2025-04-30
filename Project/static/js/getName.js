function getName() {
    $.ajax(
        {
            url: '127.0.0.1:3323/get_name',
            method: 'post',
            dataType: 'json',
            data: {text: 'Текст'},
            success: (data) => {alert(data.name)}
        }
    )
}

getName()