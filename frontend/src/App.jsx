import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import { ToastContainer } from "react-toastify";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";


function App(){

  return(

    <BrowserRouter>

      <Routes>

        <Route 
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

      </Routes>
      <ToastContainer
        position="top-right"
        autoClose={5000}
    />

    </BrowserRouter>

  )

}


export default App;