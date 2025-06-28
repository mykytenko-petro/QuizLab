import { getSlug, redirectInApp, ajaxPostRequest } from "/static/js/utils.js"

export function setQuizSettings() {
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
        const img = document.querySelector('.quizImageInput')

        ajaxPostRequest(
            "/create_quiz_api",
            json_data,
            (data) => {
                settingsDiv.innerHTML = `
                    <p>${data.name}</p>
                    <p>${data.description}</p>

                    ${(data.image === "default.png")
                        ? `<img src="/static/icons/default.png" alt="">`
                        : `<img src="/static/media/images/${data.image}" alt="image not found">`
                    }
                `

                const buttonElement = document.createElement("button")
                buttonElement.type = "button"
                buttonElement.onclick = () => { setQuizSettings() }
                buttonElement.textContent = "edit"

                settingsDiv.appendChild(buttonElement)
            },
            img.files[0]
        )
        
    }
}

const createQuestionButton = document.querySelector(".createQuestion")
createQuestionButton.addEventListener(
    "click",
    () => {
        ajaxPostRequest(
            "/create_quiz_api",
            {
                quiz_id: getSlug(),
                goal: "create",
                question: {}
            },
            (data) => {
                redirectInApp(`/question/${data.id}`)
            },
        )
    }
)