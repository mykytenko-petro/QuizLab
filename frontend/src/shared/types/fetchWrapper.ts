export interface IFetchWrapper {
    url : string
    body : FormData
    func : (data : unknown) => void
}