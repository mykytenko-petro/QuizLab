import { ajaxPostRequest } from "/static/js/ajaxUtils.js"
import { createButtonElement } from "/static/js/DOMUtils.js"
import { redirectInApp, getSlug } from "/static/js/utils.js"

function renderQuestion(data) {
    const settingsDiv = document.querySelector(".questionSettings")

    settingsDiv.innerHTML = `
        <p>${data.description}</p>

        ${(data.image === "")
            ? ``
            : `<img src="/static/media/images/${data.image}" alt="image not found">`
        }
    `

    const buttonElement = createButtonElement(setQuestionSettings, "edit")
    settingsDiv.appendChild(buttonElement)

    settingsDiv.metadata = data
}

export function loadQuestions() {
    ajaxPostRequest(
        `/api/create_quiz/quiz?goal=read&id=${getSlug()}`,
        (data) => {
            const questionsDiv = document.querySelector(".questions")

            questionsDiv.innerHTML = ""

            for (const question of data.questions) {
                const questionDiv = document.createElement("div")

                questionDiv.innerHTML += `
                    <p>${question.description}</p>

                    ${(question.image === "default.png")
                        ? `<img src="/static/icons/default.png" alt="">`
                        : `<img src="/static/media/images/${question.image}" alt="image not found">`
                    }
                    <a href="/question/${question.id}">edit</a>
                `

                const deleteButtonElement = createButtonElement(
                    () => { deleteQuestion(question.id) },
                    "delete question"
                )
                questionDiv.appendChild(deleteButtonElement)


                questionsDiv.appendChild(questionDiv)
            }
        }
    )
}


export function createQuestion() {
    ajaxPostRequest(
        `/api/create_quiz/question?goal=create&quiz_id=${getSlug()}`,
        (data) => {
            redirectInApp(`/question/${data.id}`)
        }
    )
}

export function deleteQuestion(id) {
    ajaxPostRequest(
        `/api/create_quiz/question?goal=delete&id=${id}`,
        () => {
            loadQuestions()
        }
    )
}

export function loadQuestion() {
    ajaxPostRequest(
        `/api/create_quiz/question?goal=read&id=${getSlug()}`,
        (data) => {
            const question_data = data.question

            renderQuestion(question_data)

            const linkButton = document.querySelector(".backButton")
            linkButton.href = `/quiz/${data.question.quiz_id}` 
        }
    )
}

export function setQuestionSettings() {
    const settingsDiv = document.querySelector(".questionSettings")
    const settingsForm = settingsDiv.querySelector(".questionSettingsForm")

    if (!settingsForm) {
        settingsDiv.innerHTML = `
            <form method="post" class="questionSettingsForm" enctype="multipart/form-data">
                <textarea
                    name="description"
                >${settingsDiv.metadata.description}</textarea>

                <input type="file" name="image" accept="image/*" class="questionImageInput">
            </form>
        `

        const buttonElement = createButtonElement(setQuestionSettings, "save")

        settingsDiv.appendChild(buttonElement)

    } else {
        let question_metadata = Object.fromEntries(new FormData(settingsForm))

        const imageInput = document.querySelector('.questionImageInput')

        ajaxPostRequest(
            `/api/create_quiz/question?goal=update&id=${getSlug()}`,
            (data) => { renderQuestion(data) },
            imageInput.files[0],
            question_metadata
        )
    }
}