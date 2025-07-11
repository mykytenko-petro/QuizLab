import { loadAnswers, createAnswer } from "./CRUDAnswer.js"

loadAnswers()

const createAnswerButton = document.querySelector(".createAnswer")
createAnswerButton.addEventListener(
    "click",
    () => { createAnswer() }
)