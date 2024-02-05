import React from "react";
import ReactDOM from "react-dom/client";
import './assets/styles/reset.css';
import './assets/styles/global.css';
import Router from "./components/Router";
import AuthProvider from "./components/providers/AuthProvider";


ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <AuthProvider>
            <Router />
        </AuthProvider>
    </React.StrictMode>
)