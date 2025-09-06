import { ajaxPostRequest } from "@ajaxUtils"
import { createButtonElement, createFormElement } from "@DOMUtils"
import { redirectInApp, getSlug, MetadataDiv } from "@utils"

import { IQuizPayload } from "../quiz/types"
import { IQuestionPayload } from "./types"

function renderQuestion(data : IQuestionPayload) {
    const settingsDiv = new MetadataDiv(
        document.querySelector(".questionSettings") as HTMLDivElement,
        data
    )

    settingsDiv.replaceChildren()

    const descP = document.createElement("p")
    descP.textContent = data.description
    settingsDiv.append(descP)

    console.log(!(data.image === ""))
    if (!(data.image === "")) {
        const iconImg = document.createElement("img")
        iconImg.src = `/media/images/${data.image}`
        iconImg.alt = "image not found"
        settingsDiv.append(iconImg)
    }

    const buttonElement = createButtonElement({
        func: setQuestionSettings,
        textContent: "edit"
    })

    settingsDiv.append(buttonElement)
}

export function loadQuestions() {
    ajaxPostRequest(
        `/quiz/api/quiz?goal=read&id=${getSlug()}`,
        (data : IQuizPayload) => {
            const questionsDiv = document.querySelector(".questions")

            questionsDiv.replaceChildren()

            for (const question of data.questions) {
                const questionDiv = document.createElement("div")

                const descP = document.createElement("p")
                descP.textContent = question.description
                questionDiv.appendChild(descP)

                if (!(question.image === "")) {
                    const iconImg = document.createElement("img")
                    iconImg.src = `/media/images/${question.image}`
                    iconImg.alt = "image not found"
                    questionDiv.appendChild(iconImg)
                }

                const editA = document.createElement("a")
                editA.href = `/quiz/question/${question.id}`
                editA.textContent = "edit"
                questionDiv.appendChild(editA)

                const deleteButtonElement = createButtonElement({
                    func: () => {deleteQuestion(question.id)},
                    textContent: "delete question"
                })
                questionDiv.appendChild(deleteButtonElement)


                questionsDiv.appendChild(questionDiv)
            }
        }
    )
}


export function createQuestion() {
    ajaxPostRequest(
        `/quiz/api/question?goal=create&quiz_id=${getSlug()}`,
        (data : IQuestionPayload) => {
            redirectInApp(`/quiz/question/${data.id}`)
        }
    )
}

export function deleteQuestion(id : number) {
    ajaxPostRequest(
        `/quiz/api/question?goal=delete&id=${id}`,
        () => {
            loadQuestions()
        }
    )
}

export function loadQuestion() {
    ajaxPostRequest(
        `/quiz/api/question?goal=read&id=${getSlug()}`,
        (data : object) => {
            const question_data = data["question"] as IQuestionPayload

            renderQuestion(question_data)

            const linkButton = document.querySelector(".backButton") as HTMLAnchorElement
            linkButton.href = `/quiz/edit/${data["question"].quiz_id}` 
        }
    )
}

export function setQuestionSettings() {
    const settingsDiv = new MetadataDiv(
        document.querySelector(".questionSettings") as HTMLDivElement
    )
    const existingForm = settingsDiv.querySelector(".questionSettingsForm") as HTMLFormElement | null

    if (!existingForm) {
        settingsDiv.replaceChildren()

        const settingsForm = createFormElement({
            className: "questionSettingsForm"
        })

        const descTextarea = document.createElement("textarea")
        descTextarea.name = "description"
        descTextarea.textContent = settingsDiv.getAttribute("description") as string

        const imageInput = document.createElement("input")
        imageInput.type = "file"
        imageInput.name = "image"
        imageInput.accept = "image/*"
        imageInput.className = "questionImageInput"

        settingsForm.append(
            descTextarea,
            imageInput
        )


        const buttonElement = createButtonElement({
            func: setQuestionSettings,
            textContent: "save"
        })

        settingsDiv.append(
            settingsForm,
            buttonElement
        )

    } else {
        let question_metadata = Object.fromEntries(new FormData(existingForm))

        const imageInput = document.querySelector('.questionImageInput') as HTMLInputElement

        ajaxPostRequest(
            `/quiz/api/question?goal=update&id=${getSlug()}`,
            (data : IQuestionPayload) => { renderQuestion(data) },
            imageInput.files[0],
            question_metadata
        )
    }
}