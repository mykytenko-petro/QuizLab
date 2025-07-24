import { ajaxPostRequest } from "@ajaxUtils"
import { createButtonElement, createFormElement } from "@DOMUtils"
import { redirectInApp, getSlug, MetadataDiv } from "@utils"

import { QuizPayload } from "../quiz/types"
import { QuestionPayload } from "./types"

function renderQuestion(data : QuestionPayload) {
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
        `/api/create_quiz/quiz?goal=read&id=${getSlug()}`,
        (data : QuizPayload) => {
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
                editA.href = `/question/${question.id}`
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
        `/api/create_quiz/question?goal=create&quiz_id=${getSlug()}`,
        (data : QuestionPayload) => {
            redirectInApp(`/question/${data.id}`)
        }
    )
}

export function deleteQuestion(id : number) {
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
        (data : object) => {
            const question_data = data["question"] as QuestionPayload

            renderQuestion(question_data)

            const linkButton = document.querySelector(".backButton") as HTMLAnchorElement
            linkButton.href = `/quiz/${data["question"].quiz_id}` 
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
            `/api/create_quiz/question?goal=update&id=${getSlug()}`,
            (data : QuestionPayload) => { renderQuestion(data) },
            imageInput.files[0],
            question_metadata
        )
    }
}