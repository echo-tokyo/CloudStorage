import './helloPage.css'
import { useNavigate } from 'react-router-dom'
import { useEffect } from 'react';

function HelloPage() {
    const history = useNavigate();

    useEffect(() => {
    const redirectTimer = setTimeout(() => {
      history('/login');
    }, 3000);

    return () => clearTimeout(redirectTimer);
  }, [history]);
    return(
        <div className="wrapper">
            <h1>Привет !</h1>
            <p>Cloud Storage - это возможность хранить ваши файлы на наших  <br /> серверах а ищо мы крутые</p>
        </div>
    )
}

export default HelloPage