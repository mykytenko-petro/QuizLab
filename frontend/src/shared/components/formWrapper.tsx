import { Wfetch } from "../utils";
import type { IFormWrapper } from "../types/formWrapper";


export function WForm(
  { children, url, func } : IFormWrapper
) {
  async function sendData(event : React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const formData = new FormData(event.currentTarget);
    
    await Wfetch({
      url: url,
      body: formData,
      func: (data : unknown) => {
        func?.(data)
      }
    })
  }

  return (
    <form method="post" onSubmit={sendData}>
      {children}
    </form>
  )
}