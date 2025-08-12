import { BrowserRouter, Routes, Route } from "react-router";

import HomePage from "../home/home";
import NoPage from "./noPage";
import { UserRoutes } from "../user";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />} />

        {UserRoutes()}

        <Route path="*" element={<NoPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default AppRoutes