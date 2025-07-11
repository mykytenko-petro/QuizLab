import { ajaxPostRequest } from "/static/js/ajaxUtils.js"
import { createButtonElement } from "/static/js/DOMUtils.js"
import { getSlug } from "/static/js/utils.js"

function loadAnswer(data) {
    const answerDiv = document.getElementById(`answer-${data.id}`)

    answerDiv.metadata = data

    answerDiv.innerHTML = ""
    answerDiv.innerHTML += `
        <p>${data.description}</p>

        ${(data.image === "")
            ? ``
            : `<img src="/static/media/images/${data.image}" alt="image not found">`
        }
    `

    const deleteButtonElement = createButtonElement(
        () => { deleteAnswer(data.id) },
        "delete"
    )
    answerDiv.appendChild(deleteButtonElement)
    
    const updateButtonElement = createButtonElement(
        () => { setAnswerSettings(data.id) },
        "edit"
    )
    answerDiv.appendChild(updateButtonElement)
}

export function loadAnswers() {
    ajaxPostRequest(
        `/api/create_quiz/question?goal=read&id=${getSlug()}`,
        (data) => {
            const answersDiv = document.querySelector(".answers")

            answersDiv.innerHTML = ""

            for (const answer of data.answers) {
                const answerDiv = document.createElement("div")

                answerDiv.metadata = answer
                answerDiv.id = `answer-${answer.id}`

                answerDiv.innerHTML += `
                    <p>${answer.description}</p>

                    ${(answer.image === "")
                        ? ``
                        : `<img src="/static/media/images/${answer.image}" alt="image not found">`
                    }
                `

                const deleteButtonElement = createButtonElement(
                    () => { deleteAnswer(answer.id) },
                    "delete"
                )
                answerDiv.appendChild(deleteButtonElement)
                
                const updateButtonElement = createButtonElement(
                    () => { setAnswerSettings(answer.id) },
                    "edit"
                )
                answerDiv.appendChild(updateButtonElement)

                answersDiv.appendChild(answerDiv)
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

export function deleteAnswer(id) {
    ajaxPostRequest(
        `/api/create_quiz/answer?goal=delete&id=${id}`,
        () => {
            loadAnswers()
        }
    )
}

export function setAnswerSettings(id) {
    const settingsDiv = document.getElementById(`answer-${id}`)
    console.log(settingsDiv)
    const settingsForm = settingsDiv.querySelector(".answerSettingsForm")

    if (!settingsForm) {
        settingsDiv.innerHTML = `
            <form method="post" class="answerSettingsForm" enctype="multipart/form-data">
                <textarea
                    name="description"
                >${settingsDiv.metadata.description}</textarea>

                <input
                    type="checkbox"
                    name="is_right"
                    ${
                        (settingsDiv.metadata.is_right)
                        ? "checked"
                        : ""
                    }
                >

                <input type="file" name="image" accept="image/*" class="answerImageInput">
            </form>
        `

        const buttonElement = createButtonElement(() => {setAnswerSettings(id)}, "save")

        settingsDiv.appendChild(buttonElement)

    } else {
        let answer_metadata = Object.fromEntries(new FormData(settingsForm))

        if (answer_metadata.is_right === "on") {
            answer_metadata.is_right = true
        } else {
            answer_metadata.is_right = false
        }

        const imageInput = document.querySelector('.answerImageInput')

        ajaxPostRequest(
            `/api/create_quiz/answer?goal=update&id=${id}`,
            (data) => { loadAnswer(data) },
            imageInput.files[0],
            answer_metadata
        )
    }
}