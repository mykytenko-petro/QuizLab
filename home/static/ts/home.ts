import { createQuiz } from "quiz/create_quiz/static/ts/quiz/CRUDQuiz"

const createQuizButton = document.querySelector(".createQuiz") as HTMLButtonElement
createQuizButton.addEventListener("click", () => { createQuiz() })