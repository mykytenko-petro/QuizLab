export default function RegistrationPage() {
  return (
    <>
      <form method="post">
        <p className="login">Login</p>
        <input type="text" name="login" className="login" required />

        <p className="email">Email</p>
        <input type="email" name="email" required />

        <p className="password">Password</p>
        <input type="password" name="password" required />

        <p className = "password">Password_confirm</p>
        <input type="password" name="password_confirm" required />

        <button>SEND</button>
      </form>
    </>
  )
}