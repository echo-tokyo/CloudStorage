import { useNavigate } from 'react-router-dom'
import './header.css'

function Header({changeTheme, modalOpen, profileClick}) {
    const navigate = useNavigate()

    const logoutClick = () => {
        // отправка запроса с токеном, чтобы его удалили
        navigate('/login')
    }

    const filesPush = () => {
        // отправка файлов на сервер
        console.log('отправлено')
    }

    return( 
        <header>
            <div className="header_item2">
                <div className="avatar" onClick={() => profileClick()}></div>
                <p onClick={() => logoutClick()}>Выйти</p>
            </div>
            <div className='header_item'>
                <input type="file" id="file-upload"  onChange={() => filesPush()}/>
                <label htmlFor="file-upload" className='download'>Файлы</label>
                <label htmlFor="file-upload">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none">
                    <path className='theme1' d="M18.75 15H15M15 15H11.25M15 15V11.25M15 15V18.75M21.25 26.25H8.75C5.98857 26.25 3.75 24.0114 3.75 21.25V8.75C3.75 5.98857 5.98857 3.75 8.75 3.75H21.25C24.0114 3.75 26.25 5.98857 26.25 8.75V21.25C26.25 24.0114 24.0114 26.25 21.25 26.25Z" stroke="black" strokeWidth="2" strokeLinecap="round"/>
                </svg></label>
            </div>
            <div className="header_item2">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none" onClick={() => modalOpen()}>
                    <path className='theme2' d="M22.5 7.5L21.4989 22.5161C21.4113 23.8312 21.3674 24.4889 21.0834 24.9875C20.8332 25.4265 20.456 25.7794 20.0014 25.9998C19.485 26.25 18.8259 26.25 17.5077 26.25H12.4922C11.1741 26.25 10.515 26.25 9.99861 25.9998C9.54396 25.7794 9.16674 25.4265 8.91665 24.9875C8.63259 24.4889 8.58875 23.8312 8.50107 22.5161L7.5 7.5M5 7.5H25M20 7.5L19.6617 6.48509C19.3339 5.50156 19.1699 5.0098 18.8659 4.64622C18.5974 4.32516 18.2526 4.07665 17.8631 3.92348C17.422 3.75 16.9037 3.75 15.867 3.75H14.133C13.0963 3.75 12.578 3.75 12.1369 3.92348C11.7474 4.07665 11.4026 4.32516 11.1341 4.64622C10.8301 5.0098 10.6662 5.50156 10.3383 6.48509L10 7.5" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none" onClick={() => changeTheme()}>
                    <path className='theme3' d="M15 27.5C21.9036 27.5 27.5 21.9036 27.5 15C27.5 8.09644 21.9036 2.5 15 2.5C8.09644 2.5 2.5 8.09644 2.5 15C2.5 21.9036 8.09644 27.5 15 27.5ZM15 25V5C20.5228 5 25 9.47715 25 15C25 20.5228 20.5228 25 15 25Z" fill="black" />
                </svg>
            </div>
        </header>
    )
}

export default Header