"use strict";
;
;
function loadQuiz() {
    $.ajax({
        url: '/create_quiz_api',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({
            goal: "get",
            quiz_id: window.location.href.split("/").pop(),
            quiz: {},
        }),
        success: (data) => {
            let settingsDiv = document.querySelector("#quizSettings");
            settingsDiv.innerHTML = `
                    <p>${data.name}</p>
                    <p>${data.description}</p>
                `;
            let buttonElement = document.createElement("button");
            buttonElement.type = "button";
            buttonElement.onclick = () => { setQuizSettings(); };
            buttonElement.textContent = "edit";
            settingsDiv.appendChild(buttonElement);
        },
        error: (error) => {
            console.log(error);
        }
    });
}
;
loadQuiz();
function setQuizSettings() {
    let settingsDiv = document.querySelector("#quizSettings");
    if (settingsDiv.querySelector("p")) {
        let inputElement = document.createElement("input");
        inputElement.value = settingsDiv.querySelectorAll("p")[0].textContent;
        inputElement.name = "name";
        let textAreaElement = document.createElement("textarea");
        textAreaElement.value = settingsDiv.querySelectorAll("p")[1].textContent;
        textAreaElement.name = "description";
        let buttonElement = document.createElement("button");
        buttonElement.type = "button";
        buttonElement.onclick = () => { setQuizSettings(); };
        buttonElement.textContent = "save";
        let formElement = document.createElement("form");
        formElement.id = "quizSettingsForm";
        formElement.appendChild(inputElement);
        formElement.appendChild(textAreaElement);
        formElement.appendChild(buttonElement);
        settingsDiv.innerHTML = "";
        settingsDiv.appendChild(formElement);
    }
    else {
        const formElement = document.querySelector("#quizSettingsForm");
        const form = new FormData(formElement);
        const formData = Object.fromEntries(form.entries());
        $.ajax({
            url: '/create_quiz_api',
            method: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                goal: "edit",
                quiz_id: window.location.href.split("/").pop(),
                quiz: formData
            }),
            success: (data) => {
                settingsDiv.innerHTML = `
                        <p>${data.name}</p>
                        <p>${data.description}</p>
                    `;
                let buttonElement = document.createElement("button");
                buttonElement.type = "button";
                buttonElement.onclick = () => { setQuizSettings(); };
                buttonElement.textContent = "edit";
                settingsDiv.appendChild(buttonElement);
            },
            error: (error) => {
                console.log(error);
            }
        });
    }
    ;
}
;
function deleteQuiz() {
    $.ajax({
        url: '/create_quiz_api',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({
            goal: "delete",
            quiz_id: window.location.href.split("/").pop(),
            quiz: {}
        }),
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
        data: JSON.stringify({
            goal: "create",
            quiz_id: window.location.href.split("/").pop(),
            question: {}
        }),
        success: (data) => {
            window.location.replace(`/question/${data.id}`);
        },
        error: (error) => {
            console.log(error);
        }
    });
}
;
