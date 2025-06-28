import { getSlug, ajaxPostRequest } from "/static/js/utils.js"
import { setQuestionSettings } from "./createQuestion.js"

export function loadQuestion() {
    ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "get",
            question: {
                id: getSlug()
            }
        },
        (data) => {
            // 
            const settingsDiv = document.querySelector(".questionSettings")

            settingsDiv.innerHTML = `
                <p>${data.question.description}</p>

                ${(data.question.image === "default.png")
                    ? `<img src="/static/icons/default.png" alt="">`
                    : `<img src="/static/media/images/${data.question.image}" alt="image not found">`
                }
            `

            const buttonElement = document.createElement("button")
            buttonElement.type = "button"
            buttonElement.onclick = () => { setQuestionSettings() }
            buttonElement.textContent = "edit"

            settingsDiv.appendChild(buttonElement)

            // 
            const linkButton = document.querySelector(".backButton")
            linkButton.href = `/quiz/${data.question.quiz_id}` 
        },
    )
}

loadQuestion()