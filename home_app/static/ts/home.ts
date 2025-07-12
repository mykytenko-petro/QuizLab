import { createQuiz } from "create_quiz_app/static/ts/quiz/CRUDQuiz"

const createQuizButton = document.querySelector(".createQuiz") as HTMLButtonElement
createQuizButton.addEventListener("click", () => { createQuiz() })