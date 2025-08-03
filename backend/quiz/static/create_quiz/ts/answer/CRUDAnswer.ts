import { ajaxPostRequest } from "backend/Project/static/ts/utils/ajaxUtils/index"
import { createButtonElement, createFormElement } from "backend/Project/static/ts/utils/DOMUtils/index"
import { getSlug, MetadataDiv } from "backend/Project/static/ts/utils/utils/index"

import { QuestionPayload } from "../question/types"
import { AnswerPayload } from "./types"

function loadAnswer(data : AnswerPayload) {
    const answerDiv = new MetadataDiv(
        document.getElementById(`answer-${data.id}`) as HTMLDivElement,
        data
    )

    answerDiv.replaceChildren()

    const descP = document.createElement("p")
    descP.textContent = data.description
    answerDiv.append(descP)

    if (!(data.image === "")) {
        const iconImg = document.createElement("img")
        iconImg.src = `/media/images/${data.image}`
        iconImg.alt = "image not found"
        answerDiv.append(iconImg)
    }

    const deleteButtonElement = createButtonElement({
        func: () => { deleteAnswer(data.id) },
        textContent: "delete"
    })
    answerDiv.append(deleteButtonElement)
    
    const updateButtonElement = createButtonElement({
        func: () => { setAnswerSettings(data.id) },
        textContent: "edit"
    })
    answerDiv.append(updateButtonElement)
}

export function loadAnswers() {
    ajaxPostRequest(
        `/api/create_quiz/question?goal=read&id=${getSlug()}`,
        (data : QuestionPayload) => {
            const answersDiv = document.querySelector(".answers") as HTMLDivElement

            answersDiv.replaceChildren()

            for (const answer of data.answers) {
                const answerDiv = new MetadataDiv(
                    document.createElement("div"),
                    answer
                )
 
                answerDiv.div.id = `answer-${answer.id}`

                const descP = document.createElement("p")
                descP.textContent = data.description
                answerDiv.append(descP)

                if (!(answer.image === "")) {
                    const iconImg = document.createElement("img")
                    iconImg.src = `/media/images/${answer.image}`
                    iconImg.alt = "image not found"
                    answerDiv.append(iconImg)
                }

                const deleteButtonElement = createButtonElement({
                    func: () => { deleteAnswer(answer.id) },
                    textContent: "delete"
                })
                answerDiv.append(deleteButtonElement)
                
                const updateButtonElement = createButtonElement({
                    func: () => { setAnswerSettings(answer.id) },
                    textContent: "edit"
                })
                answerDiv.append(updateButtonElement)

                answersDiv.appendChild(answerDiv.div)
            }
        }
    )
}


export function createAnswer() {
    ajaxPostRequest(
        `/api/create_quiz/answer?goal=create&question_id=${getSlug()}`,
        () => {
            loadAnswers()
        }
    )
}

export function deleteAnswer(id : number) {
    ajaxPostRequest(
        `/api/create_quiz/answer?goal=delete&id=${id}`,
        () => {
            loadAnswers()
        }
    )
}

export function setAnswerSettings(id : number) {
    const settingsDiv = new MetadataDiv(
        document.getElementById(`answer-${id}`) as HTMLDivElement
    )
    const existingForm = settingsDiv.querySelector(".answerSettingsForm") as HTMLFormElement | null

    if (!existingForm) {
        settingsDiv.replaceChildren()

        const settingsForm = createFormElement({
            className: "answerSettingsForm"
        })

        const descTextarea = document.createElement("textarea")
        descTextarea.name = "description"
        descTextarea.textContent = settingsDiv.getAttribute("description") as string

        const isRightInput = document.createElement("input")
        isRightInput.type = "checkbox"
        isRightInput.name = "is_right"
        isRightInput.checked = settingsDiv.getAttribute("is_right") as boolean

        const imageInput = document.createElement("input")
        imageInput.type = "file"
        imageInput.name = "image"
        imageInput.accept = "image/*"
        imageInput.className = "answerImageInput"

        settingsForm.append(
            descTextarea,
            isRightInput,
            imageInput
        )

        const buttonElement = createButtonElement({
            func: () => {setAnswerSettings(id)},
            textContent: "save"
        })

        settingsDiv.append(
            settingsForm,
            buttonElement
        )

    } else {
        let answer_metadata = {is_right: null}
        const raw_metadata = Object.fromEntries(new FormData(existingForm))

        if (raw_metadata.is_right === "on") {
            answer_metadata.is_right = true
        } else {
            answer_metadata.is_right = false
        }

        Object.assign(raw_metadata, answer_metadata)

        const imageInput = document.querySelector('.answerImageInput') as HTMLInputElement

        ajaxPostRequest(
            `/api/create_quiz/answer?goal=update&id=${id}`,
            (data : AnswerPayload) => { loadAnswer(data) },
            imageInput.files[0],
            raw_metadata
        )
    }
}