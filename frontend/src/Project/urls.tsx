import { BrowserRouter, Routes, Route } from "react-router";

import HomePage from "../home/home";
import LoginPage from "../user/login/login";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default AppRoutes