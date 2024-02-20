import { useNavigate } from 'react-router-dom'
import './header.css'
import axios from 'axios'

function Header({changeTheme, modalOpen, profileClick, profilePhoto, setFiles, formatFileSize, setFolders, activeFolder}) {
    const token = localStorage.getItem('token')
    const navigate = useNavigate()
    const logoutClick = () => {
        axios.post('http://79.137.204.172/api/user/logout/', token, {headers: {'Authorization': `Bearer ${token}`}})
        .catch(error => {
            console.error('Произошла ошибка при выходе ', error)
        })
        navigate('/login')
        localStorage.removeItem('token')
        localStorage.removeItem('rootDir')
    }
    
    const filesPush = (e) => {
        const file = e.target.files[0]
        const formData = new FormData()
        formData.append('file', file)
        formData.append('folder_id', activeFolder)

        axios.post('http://79.137.204.172/api/storage/upload-file-to-server/', formData, {headers: {'Authorization' : `Bearer ${token}`}})
        .then(response => {
            const newFile = {id: response.data.id, name: response.data.name, size: formatFileSize(response.data.size)}
            setFiles(prevFiles => [...prevFiles, newFile])
        })
        .catch(error => {
            console.error('Произошла ошибка при отправке файла ', error)
        })
    }
    const createFolder = () => {
        axios.post('http://79.137.204.172/api/storage/create-folder/', {parent: activeFolder, name: 'test'}, {headers: {'Authorization' : `Bearer ${token}`}})
        .then(response => {
            const newFolder = {id: response.data.id, name: response.data.name}
            setFolders(prevFolders => [...prevFolders, newFolder])
        })
    }
    return( 
        <header>
            <div className="header_item2">
                <div className="avatar modal-opener" onClick={() => profileClick()} style={{backgroundImage: `url('${profilePhoto}')`}}></div>
                <p onClick={() => logoutClick()}>Выйти</p>
            </div>
            <form className='header_item' onChange={(e) => filesPush(e)}>
                <input type="file" id="file-upload"/>
                <label htmlFor="file-upload" className='download'>Файлы</label>
                <label htmlFor="file-upload" className='label'>
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none">
                        <path className='theme1' d="M18.75 15H15M15 15H11.25M15 15V11.25M15 15V18.75M21.25 26.25H8.75C5.98857 26.25 3.75 24.0114 3.75 21.25V8.75C3.75 5.98857 5.98857 3.75 8.75 3.75H21.25C24.0114 3.75 26.25 5.98857 26.25 8.75V21.25C26.25 24.0114 24.0114 26.25 21.25 26.25Z" stroke="black" strokeWidth="2" strokeLinecap="round"/>
                    </svg>
                </label>
            </form>
            <div className="header_item2">
                <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" onClick={() => createFolder()}>
                    <path className='theme1' d="M11.25 16.25H18.75M15 12.5V20M15.0784 7.57842L14.9216 7.42158C14.4892 6.98919 14.273 6.773 14.0208 6.6184C13.797 6.48133 13.5531 6.38031 13.2981 6.31908C13.0104 6.25 12.7046 6.25 12.0931 6.25H7.75C6.34987 6.25 5.6498 6.25 5.11503 6.52249C4.64461 6.76216 4.26216 7.14461 4.02249 7.61503C3.75 8.1498 3.75 8.84986 3.75 10.25V19.75C3.75 21.1501 3.75 21.8503 4.02249 22.385C4.26216 22.8554 4.64461 23.2379 5.11503 23.4775C5.6498 23.75 6.34986 23.75 7.75 23.75H22.25C23.6501 23.75 24.3503 23.75 24.885 23.4775C25.3554 23.2379 25.7379 22.8554 25.9775 22.385C26.25 21.8503 26.25 21.1501 26.25 19.75V12.75C26.25 11.3499 26.25 10.6498 25.9775 10.115C25.7379 9.64461 25.3554 9.26216 24.885 9.02249C24.3503 8.75 23.6501 8.75 22.25 8.75H17.9069C17.2954 8.75 16.9896 8.75 16.7019 8.68092C16.4469 8.61969 16.203 8.51867 15.9792 8.3816C15.727 8.227 15.5108 8.01081 15.0784 7.57842Z" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                <svg className='modal-opener' xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none" onClick={() => modalOpen()}>
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