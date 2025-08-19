import { fetchWrapper } from "../../../shared/utils";

export default function RegistrationPage() {
  async function sendData(event : React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const formData = new FormData(event.currentTarget);
    
    fetchWrapper({
      url: "/user/register",
      body: formData,
      func: (data : unknown) => {
        console.log(data)
      }
    })
  }

  return (
    <form action="registration" method="post" onSubmit={sendData}>
      <p className="username">Username</p>
      <input type="text" name="username" className="username" required />

      <p className="email">Email</p>
      <input type="email" name="email" required />

      <p className="password">Password</p>
      <input type="password" name="password" required />

      <p className = "password">Password_confirm</p>
      <input type="password" name="password_confirm" required />

      <button>SEND</button>
    </form>
  )
}