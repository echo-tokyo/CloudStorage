import { BrowserRouter, Route, Routes } from "react-router-dom"
import Home from "./home/Home"
import Login from './auth/LoginPage'
import Reg from "./auth/RegPage"
import HelloPage from "./helloPage/HelloPage"

function Router () {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<Home />} path='/'/>
                <Route element={<Login />} path='/login'/>
                <Route element={<Reg />} path="/reg"/>
                <Route element={<HelloPage />} path='/hello'/>
                <Route path="*" element={<div>404 Not found</div>} />
            </Routes>
        </BrowserRouter>
    )
}

export default Router