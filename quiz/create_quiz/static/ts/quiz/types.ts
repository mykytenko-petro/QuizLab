import { IQuestionPayload } from "../question/types"

export interface IQuizPayload {
    id : number
    name : string
    description : string
    image : string
    questions : Array<IQuestionPayload>
}