import { ajaxPostRequest } from "/static/js/ajaxUtils.js"
import { createButtonElement } from "/static/js/DOMUtils.js"
import { redirectInApp, getSlug } from "/static/js/utils.js"

function renderQuiz(data) {
    const settingsDiv = document.querySelector(".quizSettings")

    settingsDiv.innerHTML = `
        <p>${data.name}</p>
        <p>${data.description}</p>

        ${(data.image === "default.png")
            ? `<img src="/static/icons/default.png" alt="">`
            : `<img src="/static/media/images/${data.image}" alt="image not found">`
        }
    `

    const buttonElement = createButtonElement(setQuizSettings, "edit")
    settingsDiv.appendChild(buttonElement)

    settingsDiv.metadata = data
}

export function loadQuiz() {
    ajaxPostRequest(
        `/api/create_quiz/quiz?goal=read&id=${getSlug()}`,
        (data) => {
            renderQuiz(data.quiz)
        }
    )
}

export function createQuiz() {
    ajaxPostRequest(
        "/api/create_quiz/quiz?goal=create",
        (data) => {
            redirectInApp(`/quiz/${data.id}`)
        }
    )
}

export function deleteQuiz() {
    ajaxPostRequest(
        `/api/create_quiz/quiz?goal=delete&id=${getSlug()}`,
        () => {
            redirectInApp("/")
        }
    )
}

export function setQuizSettings() {
    const settingsDiv = document.querySelector(".quizSettings")
    const settingsForm = settingsDiv.querySelector(".quizSettingsForm")

    if (!settingsForm) {
        settingsDiv.innerHTML = `
            <form method="post" class="quizSettingsForm" enctype="multipart/form-data">
                <input
                    type="text"
                    value="${settingsDiv.metadata.name}"
                    name="name"
                >

                <textarea
                    name="description"
                >${settingsDiv.metadata.description}</textarea>

                <input type="file" name="image" accept="image/*" class="quizImageInput">
            </form>
        `

        const buttonElement = createButtonElement(setQuizSettings, "save")

        settingsDiv.appendChild(buttonElement)

    } else {
        let quiz_metadata = Object.fromEntries(new FormData(settingsForm))

        const imageInput = document.querySelector('.quizImageInput')

        ajaxPostRequest(
            `/api/create_quiz/quiz?goal=update&id=${getSlug()}`,
            (data) => { renderQuiz(data) },
            imageInput.files[0],
            quiz_metadata
        )
    }
}