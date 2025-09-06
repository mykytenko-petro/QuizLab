import { ajaxPostRequest, ajaxGetRequest } from "@ajaxUtils"
import { createButtonElement, createFormElement } from "@DOMUtils"
import { redirectInApp, getSlug, MetadataDiv } from "@utils"

import { IQuizPayload } from "./types"

function renderQuiz(data : IQuizPayload) {
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
    ajaxGetRequest(
        `/quiz/api/quiz?goal=read&id=${getSlug()}`,
        (data) => {
            renderQuiz(data["quiz"] as IQuizPayload)
        }
    )
}

export function createQuiz() {
    ajaxGetRequest(
        "/quiz/api/quiz?goal=create",
        (data : IQuizPayload) => {
            redirectInApp(`/quiz/edit/${data.id}`)
        }
    )
}

export function deleteQuiz() {
    ajaxGetRequest(
        `/quiz/api/quiz?goal=delete&id=${getSlug()}`,
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
            `/quiz/api/quiz?goal=update&id=${getSlug()}`,
            (data : IQuizPayload) => { renderQuiz(data) },
            imageInput.files[0],
            quiz_metadata
        )
    }
}