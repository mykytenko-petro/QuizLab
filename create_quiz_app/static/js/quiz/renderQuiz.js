import { setQuizSettings } from "./createQuiz.js"
import { getSlug, ajaxPostRequest } from "/static/js/utils.js"

function loadQuiz() {
    ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "get",
            quiz: {
                id: getSlug()
            }
        },
        (data) => {
            const quiz_data = data.quiz

            const settingsDiv = document.querySelector(".quizSettings")

            settingsDiv.innerHTML = `
                <p>${quiz_data.name}</p>
                <p>${quiz_data.description}</p>

                ${(data.image === "default.png")
                    ? `<img src="/static/icons/default.png" alt="">`
                    : `<img src="/static/media/images/${quiz_data.image}" alt="image not found">`
                }
            `

            const buttonElement = document.createElement("button")
            buttonElement.type = "button"
            buttonElement.onclick = () => { setQuizSettings() }
            buttonElement.textContent = "edit"

            settingsDiv.appendChild(buttonElement)

            loadQuestions()
        },
    )
}

loadQuiz()

function loadQuestions() {
    ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "get",
            quiz: {
                id: getSlug()
            }
        },
        (data) => {
            data = data.questions

            const questionsDiv = document.querySelector(".questions")

            if (!data.length) {
                questionsDiv.innerHTML = ""
            }

            for (const question of data) {
                const questionDiv = document.createElement("div")
                questionDiv.innerHTML += `
                    <p>${question.description}</p>

                    ${(question.image === "default.png")
                        ? `<img src="/static/icons/default.png" alt="">`
                        : `<img src="/static/media/images/${question.image}" alt="image not found">`
                    }
                    <a href="/question/${question.id}">edit</a>
                    
                `
                const buttonElement = document.createElement("button")
                buttonElement.type = "button"
                buttonElement.onclick = () => { deleteQuestion(question.id) }
                buttonElement.textContent = "delete question"

                questionDiv.appendChild(buttonElement)
                
                questionsDiv.appendChild(questionDiv)
            }
        }
    )
}

function deleteQuestion(id) {
    ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "delete", 
            question: {
                id: id
            }
        },
        (data) => {
            loadQuestions(data)
        }
    )
}