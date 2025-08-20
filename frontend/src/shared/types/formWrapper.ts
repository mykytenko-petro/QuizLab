export interface IFormWrapper {
    children : React.ReactNode
    url : string
    func? : (data : unknown) => void
}