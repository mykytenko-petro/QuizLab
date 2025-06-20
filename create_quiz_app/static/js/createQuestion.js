import { ajaxPostRequest } from "./quizUtils.js"
import { getSlug, redirectInApp } from "/static/js/utils.js"

function loadQuiz() {
    let dataToSend = new FormData()
    dataToSend.append(
        "data",
        JSON.stringify(
            {
                goal: "get",
                quiz: {
                    id: getSlug()
                }
            }
        )
    )

    ajaxPostRequest(
        dataToSend,
        (data) => {
            const settingsDiv = document.querySelector(".quizSettings")

            settingsDiv.innerHTML = `
                <p>${data.name}</p>
                <p>${data.description}</p>
                <img src="/static/media/images/${data.image}" alt="">
            `

            const buttonElement = document.createElement("button")
            buttonElement.type = "button"
            buttonElement.onclick = () => { setQuizSettings() }
            buttonElement.textContent = "edit"

            settingsDiv.appendChild(buttonElement)
        },
    )
}

loadQuiz()

function setQuizSettings() {
    const settingsDiv = document.querySelector(".quizSettings")

    if (!settingsDiv.querySelector(".quizSettingsForm")) {
        settingsDiv.innerHTML = `
            <form method="post" class="quizSettingsForm" enctype="multipart/form-data">
                <input
                    type="text"
                    value="${settingsDiv.querySelectorAll("p")[0].textContent}"
                    name= "name"
                >

                <textarea
                    name="description"
                    value="${settingsDiv.querySelectorAll("p")[1].textContent}"
                ></textarea>

                <input type="file" name="image" accept="image/*" class="quizImageInput">
            </form>
        `

        const buttonElement = document.createElement("button")
        buttonElement.type = "button"
        buttonElement.onclick = () => { setQuizSettings() }
        buttonElement.textContent = "save"

        settingsDiv.appendChild(buttonElement)

    } else {
        let dataToSend = new FormData()

        let json_data = {
            goal: "edit", 
            quiz: Object.assign(
                {
                    id: getSlug()
                },
                Object.fromEntries(
                    new FormData(
                        document.querySelector(".quizSettingsForm")
                    )
                )
            )
        }

        console.log(json_data)

        dataToSend.append("data", JSON.stringify(json_data))

        const img = document.querySelector('.quizImageInput')

        dataToSend.append("image", img.files[0])

        ajaxPostRequest(
            dataToSend,
            (data) => {
                settingsDiv.innerHTML = `
                    <p>${data.name}</p>
                    <p>${data.description}</p>
                    <img src="/static/media/images/${data.image}" alt="">
                `

                const buttonElement = document.createElement("button")
                buttonElement.type = "button"
                buttonElement.onclick = () => { setQuizSettings() }
                buttonElement.textContent = "edit"

                settingsDiv.appendChild(buttonElement)
            }
        )
    }
}


const createQuestionButton = document.querySelector(".createQuestion")
createQuestionButton.addEventListener(
    "click",
    () => {
        ajaxPostRequest(
            {
                goal: "create",
                quiz_id: getSlug(),
                question: {}
            },
            (data) => {
                redirectInApp(`/question/${data.id}`)
            }
        )
    }
)