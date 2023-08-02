//pages imports
import Login from "./Pages/Login/login";
import Signup from "./Pages/SignUp/signup";
import Home from "./Pages/Home/home";
import Profile from "./Pages/Profile/profile";

//components imports
import NavBar from "./Components/NavBar/navbar";

//styles imports
import "./theme.scss"

//react imports
import {
  createBrowserRouter,
  Navigate,
  RouterProvider,
  Outlet
} from "react-router-dom";

import { useContext } from "react";
import { DarkModeContext } from "./Context/darkmodecontext";
import { AuthContext } from "./Context/authentication";

function App() {

  //const {currentUser} = useContext(AuthContext);  -  auth function
  const currentUser = true;

  const {DarkMode} = useContext(DarkModeContext)
  console.log(DarkMode)

  const Layout = ()=>{
    return(
      <div className={`theme-${DarkMode?"dark":"light"}`}>
        <NavBar/>
        {/* <div style={{flex: 6}}> */}
          <Outlet/>
        {/* </div> */}
      </div>
    )
  }

  const ProtectedRoute = ({children}) =>{
    if(!currentUser){
      return <Navigate to="/login"/>
    }
    return children;
  }

  const router = createBrowserRouter([
    {
      //path:"/",
      element: (
      <ProtectedRoute>
        <Layout/>
      </ProtectedRoute>
      ),
      children: [
        {
          path:"/",
          element:<Home/>
        },
        {
          path:"/profile/",
          element:<Profile/>
        }
      ]
    },
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
