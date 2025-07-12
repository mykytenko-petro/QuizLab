import { loadAnswers, createAnswer } from "./CRUDAnswer"

loadAnswers()

const createAnswerButton = document.querySelector(".createAnswer") as HTMLButtonElement
createAnswerButton.addEventListener("click", () => { createAnswer() })