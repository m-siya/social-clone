import Login from "./Pages/Login/login";
import Signup from "./Pages/SignUp/signup";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

function App() {
  const router = createBrowserRouter([
    {
      path: "/login",
      element: <Login/>,
    },
    {
      path:"/signup",
      element: <Signup/>,
    },
  ]);

  return (
    <div>
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
