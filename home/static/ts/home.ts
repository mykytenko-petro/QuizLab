import { createQuiz } from "quiz/static/create_quiz/ts/quiz/CRUDQuiz"

const createQuizButton = document.querySelector(".createQuiz") as HTMLButtonElement
createQuizButton.addEventListener("click", () => { createQuiz() })