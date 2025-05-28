function setQuizSettings() {
    const form = new FormData(document.querySelector("#quizSettings"));
    const formData = Object.fromEntries(form.entries());

    $.ajax(
        {
            url: '/create_quiz_api',
            method: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(
                {
                    goal: "edit",
                    quiz_id: window.location.href.split("/").pop(),
                    quiz: formData
                }
            ),
            success: (data) => {
                console.log(data);
            },
            error: (error) => {
                console.log(error);
            }
        }
    );
};

function deleteQuiz() {
    $.ajax(
        {
            url: '/create_quiz_api',
            method: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(
                {
                    goal: "delete",
                    quiz_id: window.location.href.split("/").pop(),
                    quiz: {}
                }
            ),
            success: (data) => {
                window.location.replace("/");
            },
            error: (error) => {
                console.log(error);
            }
        }
    );
};

function create_question() {
    $.ajax(
        {
            url: '/create_quiz_api',
            method: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(
                {
                    goal: "create",
                    quiz_id: window.location.href.split("/").pop(),
                    quiz: {}
                }
            ),
            success: (data) => {
                window.location.replace("/");
            },
            error: (error) => {
                console.log(error);
            }
        }
    );
}