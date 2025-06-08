export interface ApiOutput {
    quiz?: QuizOutput;
    id?: number;
}

export interface QuizOutput {
    id: number;
    name: string;
    description: string;
}

export interface QuestionOutput {
    id: number
    name: string
    description: string
}