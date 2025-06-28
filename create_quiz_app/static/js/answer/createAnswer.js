import { getSlug, ajaxPostRequest } from "/static/js/utils.js"
import { loadAnswers, loadAnswer } from "./renderAnswer.js"

const createButton = document.querySelector(".createAnswer")
createButton.addEventListener(
    "click",
    () => {
        ajaxPostRequest(
            "/create_quiz_api",
            {
                question_id: getSlug(),
                goal: "create",
                answer: {}
            },
            (data) => {
                loadAnswers()
            }
        )
    }
)

export function setAnswerSettings(id) {
    const settingsDiv = document.getElementById(`${id}`)

    if (!settingsDiv.querySelector(".answerSettingsForm")) {
        settingsDiv.innerHTML = `
            <form method="post" class="answersSettingsForm" enctype="multipart/form-data">
                <textarea
                    name="description"
                    value=""
                ></textarea>
                
                <input
                    type="checkbox"
                    name="is_right"
                >
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
                <label class="form-check-label" for="flexSwitchCheckChecked">is right</label>

                <input type="file" name="image" accept="image/*" class="answersImageInput">
            </form>
        `

        const buttonElement = document.createElement("button")
        buttonElement.type = "button"
        buttonElement.onclick = () => { setAnswerSettings() }//
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
                        document.querySelector("answersSettingsForm")
                    )
                )
            )
        }
        const img = document.querySelector('.answersImageInput')

        ajaxPostRequest(
            "/create_quiz_api",
            json_data,
            (data) => {
                loadAnswer(data.id)
            },
            img.files[0]
        )
    }
}

export function deleteAnswer(id) {
     ajaxPostRequest(
        "/create_quiz_api",
        {
            goal: "delete", 
            answer: {
                id: id
            }
        },
        (data) => {
            loadAnswers()
        }
    )

}