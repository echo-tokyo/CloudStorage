import axios from 'axios'
import './modal.css'
import ModalFile from './modalFile/ModalFile'
import ModalFolder from './modalFolder/ModalFolder'

function Modal ({trashFiles, setTrashFiles, setFiles, setTrashFolders, trashFolders, setFolders}) {
    const trashRemove = () => {
        axios.delete('http://79.137.204.172/api/storage/clear-trash/', {headers:{Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(() => {
            setTrashFiles('')
            setTrashFolders('')
        })
        .catch(error => {
            console.error('Произошла ошибка при удалении ', error)
        })
    }
    return(
        <div className="modal-window">
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
            </div>
        </div>
    )
}

export default Modal