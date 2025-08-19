import { Route } from "react-router";

import LoginPage from "./login/login";
import RegistrationPage from "./registration/components/registration";

export function UserRoutes() {
  return (
    <>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/registration" element={<RegistrationPage />} />
    </>
  )
}