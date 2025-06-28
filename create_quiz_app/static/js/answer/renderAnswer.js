import { getSlug, ajaxPostRequest } from "/static/js/utils.js"
import { setAnswerSettings, deleteAnswer } from "./createAnswer.js"

const answersDiv = document.querySelector(".answers")

export function loadAnswers() {
    ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "get",
            question: {
                id: getSlug()
            }
        },
        (data) => {
            if (!data.lenght) {
                answersDiv.innerHTML = ""
            }

            for (const answer of data.answers) {
                loadAnswer(answer.id)
            }
        }
    )
}

loadAnswers()

export function loadAnswer(id) {
    ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "get",
            answer: {
                id: id
            }
        },
        (data) => {
            const answerDiv = document.createElement("div")

            answerDiv.id = data.id

            answerDiv.innerHTML += `
                <p>${data.description}</p>

                
                <input
                    type="checkbox"
                    name="is_right"
                    ${(data.is_right)
                        ? "checked"
                        : ""
                    }
                >
            `
            const editButton = document.createElement("button")
            editButton.type = "button"
            editButton.onclick = () => { setAnswerSettings(id) }
            editButton.textContent = "edit"
            answerDiv.appendChild(editButton)
            
            const deleteButton = document.createElement("button")
            deleteButton.type = "button"
            deleteButton.onclick = () => { deleteAnswer(data.id) }
            deleteButton.textContent = "delete answer"
            answerDiv.appendChild(deleteButton)
            
            answersDiv.appendChild(answerDiv)
        }
    )
}