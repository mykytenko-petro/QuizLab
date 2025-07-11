import { loadQuiz, deleteQuiz } from "./CRUDQuiz.js"
import { loadQuestions, createQuestion } from "../question/CRUDQuestion.js"

loadQuiz()
loadQuestions()

const deleteQuizButton = document.querySelector(".deleteQuiz")
deleteQuizButton.addEventListener("click", () => { deleteQuiz() })

const createQuestionButton = document.querySelector(".createQuestion")
createQuestionButton.addEventListener("click", () => { createQuestion() })