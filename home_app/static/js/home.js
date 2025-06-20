import { ajaxPostRequest } from "/create_quiz/static/js/quizUtils.js"
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
                    quiz: {
                        
                    }
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
