"use strict";
function loadQuiz() {
    $.ajax({
        url: '/create_quiz_api',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: (data) => {
            console.log(data);
        },
        error: (error) => {
            console.log(error);
        }
    });
}
;
function setQuizSettings() {
    const formElement = document.querySelector("#quizSettings");
    const form = new FormData(formElement);
    const formData = Object.fromEntries(form.entries());
    $.ajax({
        url: '/create_quiz_api',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            goal: "edit",
            quiz_id: window.location.href.split("/").pop(),
            quiz: formData
        },
        success: (data) => {
            console.log(data);
        },
        error: (error) => {
            console.log(error);
        }
    });
}
;
function deleteQuiz() {
    $.ajax({
        url: '/create_quiz_api',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            goal: "delete",
            quiz_id: window.location.href.split("/").pop(),
            quiz: {}
        },
        success: () => {
            window.location.replace("/");
        },
        error: (error) => {
            console.log(error);
        }
    });
}
;
function createQuestion() {
    $.ajax({
        url: '/create_quiz_api',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            goal: "create",
            quiz_id: window.location.href.split("/").pop(),
            question: {}
        },
        success: (data) => {
            window.location.replace(`/question/${data.id}`);
        },
        error: (error) => {
            console.log(error);
        }
    });
}
