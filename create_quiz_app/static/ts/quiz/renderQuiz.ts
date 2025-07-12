import { loadQuiz, deleteQuiz } from "./CRUDQuiz"
import { loadQuestions, createQuestion } from "../question/CRUDQuestion"

loadQuiz()
loadQuestions()

const deleteQuizButton = document.querySelector(".deleteQuiz") as HTMLButtonElement
deleteQuizButton.addEventListener("click", () => { deleteQuiz() })

const createQuestionButton = document.querySelector(".createQuestion") as HTMLButtonElement
createQuestionButton.addEventListener("click", () => { createQuestion() })