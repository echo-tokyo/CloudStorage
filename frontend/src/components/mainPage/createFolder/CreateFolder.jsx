import axios from 'axios'
import './createFolder.css'

const CreateFolder = ({activeFolder, setFolders, setCreateFolder}) => {
	const createNewFolder = (e) => {
		e.preventDefault()
		setCreateFolder(false)
		const folderName = e.target.name.value

		axios.post('http://79.137.204.172/api/storage/create-folder/', {parent: activeFolder, name: folderName}, {headers: {'Authorization' : `Bearer ${localStorage.getItem('token')}`}})
        .then(response => {
            const newFolder = {id: response.data.id, name: response.data.name}
            setFolders(prevFolders => [...prevFolders, newFolder])
        })
	}
	return (
		<div className="modal-folder">
            <div className="titles">
                <p>Создание папки</p>
            </div>
			<form className='modal-form' onSubmit={(e) => createNewFolder(e)}>
				<input type="text" name='name' placeholder='Название папки'/>
				<input type="submit" value="Создать"/>
			</form>
        </div>
	)
}

export default CreateFolder