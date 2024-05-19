import axios from 'axios'
import './modal.css'
import ModalFile from './modalFile/ModalFile'
import ModalFolder from './modalFolder/ModalFolder'
import { useEffect } from 'react'

function Modal ({trashFiles, setTrashFiles, setFiles, setTrashFolders, trashFolders, setFolders, formatFileSize}) {
    const trashRemove = () => {
        axios.delete('https://best-edu-server.ru/api/storage/clear-trash/', {headers:{Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(() => {
            setTrashFiles('')
            setTrashFolders('')
        })
        .catch(error => {
            console.error('Произошла ошибка при удалении ', error)
        })
    }
    const handleModalClick = (event) => {
        event.stopPropagation()
    }

    useEffect(() => {
        axios.post('https://best-edu-server.ru/api/storage/get-trash/', null, {headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`}})
        .then(response => {
            const files = response.data.files.map(file => (
                {
                    id: file.id,
                    name: file.name,
                    size: formatFileSize(file.size)
                }
            ))
            const folders = response.data.folders.map(folder => (
                {
                    id: folder.id,
                    name: folder.name,
                }
            ))
            setTrashFiles(files)
            setTrashFolders(folders)
        })
        .catch(error => {
            console.error('Произошла ошибка при получении удаленных файлов ', error)
        })
    }, [])

    return(
        <div className="modal-window" onClick={event => handleModalClick(event)}>
            <div className="titles">
                <p>Корзина</p>
                <p className='subtitle' onClick={()=> trashRemove()}>Очистить</p>
            </div>
            <div className="files">
                {trashFiles.length > 0 && (
                    trashFiles.map(file => <ModalFile key={file.id} file={file} setTrashFiles={setTrashFiles} setFiles={setFiles}/>)
                )}
                {trashFolders.length > 0 && (
                    trashFolders.map(folder => <ModalFolder key={folder.id} folder={folder} setTrashFolders={setTrashFolders} setFolders={setFolders} trashFolders={trashFolders}/>)
                )}
                {trashFolders.length < 1 && trashFiles.length < 1 && (
                    <p style={{display: 'flex', justifyContent:'center'}}>There are no files</p>
                )}
            </div>
        </div>
    )
}

export default Modal