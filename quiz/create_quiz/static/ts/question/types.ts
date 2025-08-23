import { IAnswerPayload } from "../answer/types"

export interface IQuestionPayload {
    id : number
    description : string
    image : string
    answers : Array<IAnswerPayload>
}