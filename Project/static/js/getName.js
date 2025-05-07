function getName() {
    $.ajax(
        {
            url: '/get_name',
            method: 'post',
            dataType: 'json',
            success: (data) => {
                userLink = document.querySelector("#user");
                userLink.textContent = data.name;
            },
            error: (error) => {
                alert("error:" + error);
            }
        }
    );
};

getName();