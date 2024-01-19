import React from "react";
import ReactDOM from "react-dom/client";
import './assets/styles/reset.css';
import './assets/styles/global.css';
import Home from "./components/home/Home";

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Home />
    </React.StrictMode>
)