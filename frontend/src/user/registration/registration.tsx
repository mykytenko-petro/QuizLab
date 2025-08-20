import { WForm } from "../../shared/components/formWrapper"


export function RegistrationPage() {
  return (
    <WForm url="/user/register" func={(data) => {console.log(data)}}>
      <p className="username">Username</p>
      <input type="text" name="username" className="username" required />

      <p className="email">Email</p>
      <input type="email" name="email" required />

      <p className="password">Password</p>
      <input type="password" name="password" required />

      <p className = "password">Password_confirm</p>
      <input type="password" name="password_confirm" required />

      <button>SEND</button>
    </WForm>
  )
}