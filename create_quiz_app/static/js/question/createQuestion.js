import { getSlug, ajaxPostRequest } from "/static/js/utils.js"

export function setQuestionSettings() {
    const settingsDiv = document.querySelector(".questionSettings")

    if (!settingsDiv.querySelector(".questionSettingsForm")) {
        settingsDiv.innerHTML = `
            <form method="post" class="questionSettingsForm" enctype="multipart/form-data">
                <textarea
                    name="description"
                    value="${settingsDiv.querySelectorAll("p")[0].textContent}"
                ></textarea>

                <input type="file" name="image" accept="image/*" class="questionImageInput">
            </form>
        `

        const buttonElement = document.createElement("button")
        buttonElement.type = "button"
        buttonElement.onclick = () => { setQuestionSettings() }
        buttonElement.textContent = "save"

        settingsDiv.appendChild(buttonElement)

    } else {
        let json_data = {
            goal: "edit", 
            question: Object.assign(
                {
                    id: getSlug()
                },
                Object.fromEntries(
                    new FormData(
                        document.querySelector(".questionSettingsForm")
                    )
                )
            )
        }
        const img = document.querySelector('.questionImageInput')

        ajaxPostRequest(
            "/create_quiz_api",
            json_data,
            (data) => {
                settingsDiv.innerHTML = `
                    <p>${data.description}</p>

                    ${(data.image === "default.png")
                        ? `<img src="/static/icons/default.png" alt="">`
                        : `<img src="/static/media/images/${data.image}" alt="image not found">`
                    }
                `

                const buttonElement = document.createElement("button")
                buttonElement.type = "button"
                buttonElement.onclick = () => { setQuestionSettings() }
                buttonElement.textContent = "edit"

                settingsDiv.appendChild(buttonElement)
            },
            img.files[0]
        )
    }
}