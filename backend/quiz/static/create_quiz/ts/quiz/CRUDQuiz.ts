import { ajaxPostRequest } from "backend/Project/static/ts/utils/ajaxUtils/index"
import { createButtonElement, createFormElement } from "backend/Project/static/ts/utils/DOMUtils/index"
import { redirectInApp, getSlug, MetadataDiv } from "backend/Project/static/ts/utils/utils/index"

import { QuizPayload } from "./types"

function renderQuiz(data : QuizPayload) {
    const settingsDiv = new MetadataDiv(
        document.querySelector(".quizSettings") as HTMLDivElement,
        data
    )

    settingsDiv.replaceChildren()

    const nameP = document.createElement("p")
    nameP.textContent = data.name

    const descP = document.createElement("p")
    descP.textContent = data.description

    const iconImg = document.createElement("img")
    if (data.image === "default.png") {
        iconImg.src = "/static/icons/default.png"
    } else {
        iconImg.src = `/media/images/${data.image}`
        iconImg.alt = "image not found"
    }

    const createButton = createButtonElement({
        func: setQuizSettings,
        textContent: "edit"
    })

    settingsDiv.append(
        nameP,
        descP,
        iconImg,
        createButton
    )
}


export function loadQuiz() {
    ajaxPostRequest(
        `/api/create_quiz/quiz?goal=read&id=${getSlug()}`,
        (data) => {
            renderQuiz(data["quiz"] as QuizPayload)
        }
    )
}

export function createQuiz() {
    ajaxPostRequest(
        "/api/create_quiz/quiz?goal=create",
        (data : QuizPayload) => {
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
    const settingsDiv = new MetadataDiv(
        document.querySelector(".quizSettings")
    )
    const existingForm = settingsDiv.querySelector(".quizSettingsForm") as HTMLFormElement | null

    if (!existingForm) {
        settingsDiv.replaceChildren()

        const settingsForm = createFormElement({
            className: "quizSettingsForm"
        })

        const nameInput = document.createElement("input")
        nameInput.type = "text"
        nameInput.value = settingsDiv.getAttribute("name") as string
        nameInput.name = "name"

        const descTextarea = document.createElement("textarea")
        descTextarea.name = "description"
        descTextarea.textContent = settingsDiv.getAttribute("description") as string

        const imageInput = document.createElement("input")
        imageInput.type = "file"
        imageInput.name = "image"
        imageInput.accept = "image/*"
        imageInput.className = "quizImageInput"

        settingsForm.append(
            nameInput,
            descTextarea,
            imageInput
        )


        const buttonElement = createButtonElement({
            func: setQuizSettings,
            textContent: "save"
        })

        settingsDiv.append(
            settingsForm,
            buttonElement
        )

    } else {
        let quiz_metadata = Object.fromEntries(new FormData(existingForm))

        const imageInput = document.querySelector('.quizImageInput') as HTMLInputElement

        ajaxPostRequest(
            `/api/create_quiz/quiz?goal=update&id=${getSlug()}`,
            (data : QuizPayload) => { renderQuiz(data) },
            imageInput.files[0],
            quiz_metadata
        )
    }
}