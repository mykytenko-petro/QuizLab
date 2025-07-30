import { QuestionPayload } from "../question/types"

export interface QuizPayload {
    id : number
    name : string
    description : string
    image : string
    questions : Array<QuestionPayload>
}