import Login from "./Pages/Login/login";
import Signup from "./Pages/SignUp/signup";
import NavBar from "./Components/NavBar/navbar";
import Home from "./Pages/Home/home";
import "./theme.scss"
//import Profile from "./Pages/Profile/profile"
import {
  createBrowserRouter,
  Navigate,
  RouterProvider,
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
        <div style={{flex: 6}}>
          {/* <Outlet/> */}
        </div>
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
      path:"/",
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
        // {
        //   path:"/profile/:id",
        //   element:<Profile/>
        // }
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
