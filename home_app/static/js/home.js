import { createQuiz } from "/create_quiz/static/js/quiz/CRUDQuiz.js"

const createQuizButton = document.querySelector(".createQuiz")
createQuizButton.addEventListener("click", () => { createQuiz() })