import { AnswerPayload } from "../answer/types"

export interface QuestionPayload {
    id : number
    description : string
    image : string
    answers : Array<AnswerPayload>
}