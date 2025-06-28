import { ajaxPostRequest } from "/static/js/utils.js"
import { redirectInApp } from "/static/js/utils.js"

const createButton = document.querySelector(".createQuiz")
createButton.addEventListener(
    "click",
    () => {
        let dataToSend = new FormData()
        dataToSend.append(
            "data",
            JSON.stringify(
                {
                    goal: "create",
                    quiz: {}
                }
            )
        )

        ajaxPostRequest(  
            dataToSend,
            (data) => {
                redirectInApp(`/quiz/${data.id}`)
            }
        )
    }
)
