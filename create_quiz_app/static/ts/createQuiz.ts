interface QuizOutput {
    id: number;
    name: string;
    description: string;
};

interface ApiOutcome {
    quiz?: QuizOutput;
    id?: number;
};

function loadQuiz() {
    $.ajax(
        {
            url: '/create_quiz_api',
            method: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(
                {
                    goal: "get",
                    quiz_id: window.location.href.split("/").pop(),
                    quiz: {},
                }
            ),
            success: (data : QuizOutput) => {
                let settingsDiv = document.querySelector("#quizSettings") as HTMLDivElement;

                settingsDiv.innerHTML = `
                    <p>${data.name}</p>
                    <p>${data.description}</p>
                `;

                let buttonElement = document.createElement("button");
                buttonElement.type = "button";
                buttonElement.onclick = () => { setQuizSettings() };
                buttonElement.textContent = "edit";

                settingsDiv.appendChild(buttonElement);
            },
            error: (error : Object) => {
                console.log(error);
            }
        }
    );
};

loadQuiz();

function setQuizSettings() {
    let settingsDiv = document.querySelector("#quizSettings") as HTMLDivElement;

    if (settingsDiv.querySelector("p")) {
        let inputElement = document.createElement("input");
        inputElement.value = settingsDiv.querySelectorAll("p")[0].textContent as string;
        inputElement.name = "name";

        let textAreaElement = document.createElement("textarea");
        textAreaElement.value = settingsDiv.querySelectorAll("p")[1].textContent as string;
        textAreaElement.name = "description";

        let buttonElement = document.createElement("button");
        buttonElement.type = "button";
        buttonElement.onclick = () => { setQuizSettings() };
        buttonElement.textContent = "save";

        let formElement = document.createElement("form") as HTMLFormElement;
        formElement.id = "quizSettingsForm";
        formElement.appendChild(inputElement);
        formElement.appendChild(textAreaElement);
        formElement.appendChild(buttonElement);

        settingsDiv.innerHTML = "";
        settingsDiv.appendChild(formElement);

    } else {
        const formElement = document.querySelector("#quizSettingsForm") as HTMLFormElement;
        const form = new FormData(formElement);
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
                success: (data : QuizOutput) => {
                    settingsDiv.innerHTML = `
                        <p>${data.name}</p>
                        <p>${data.description}</p>
                    `;
                    let buttonElement = document.createElement("button");
                    buttonElement.type = "button";
                    buttonElement.onclick = () => { setQuizSettings() };
                    buttonElement.textContent = "edit";

                    settingsDiv.appendChild(buttonElement);
                },
                error: (error : Object) => {
                    console.log(error);
                }
            }
        );
    };
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
            success: () => {
                window.location.replace("/");
            },
            error: (error : Object) => {
                console.log(error);
            }
        }
    );
};

function createQuestion() {
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
                    question: {}
                }
            ),
            success: (data : ApiOutcome) => {
                window.location.replace(`/question/${data.id}`);
            },
            error: (error : Object) => {
                console.log(error);
            }
        }
    );
};