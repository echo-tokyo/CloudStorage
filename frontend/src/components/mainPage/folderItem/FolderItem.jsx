import axios from 'axios'

const FolderItem = ({folder, getFolderData, setFolders, setTrashFolders}) => {
	const handleRemove = (event) => {
		event.stopPropagation()
		setFolders(prev => prev.filter((el) => el.id !== folder.id))
        const token = localStorage.getItem('token')
        axios.put('http://79.137.204.172/api/storage/move-folder-to-trash/', {"id": folder.id}, {headers: {"Authorization": `Bearer ${token}`}})
        .then(() => {
            const newFolder = {id: folder.id, name: folder.name}
            setTrashFolders(prevFolders => [...prevFolders, newFolder])
        })
        .catch(error => {
            console.error('Произошла ошибка при удалении файла ', error)
        })
	}
	return (
		<div className="file-item" style={{cursor:'pointer'}} onClick={() => getFolderData(folder.id)}>
			<p>{folder.name}</p>
			<div className="file-item_item">
				<div className="file-item_item2">
					<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none" onClick={(event) => handleRemove(event)}>
						<path className='theme4' d="M23.4986 21.5431C23.7839 21.8517 23.9386 22.2586 23.9305 22.6787C23.9223 23.0988 23.7518 23.4995 23.4548 23.7967C23.1578 24.0939 22.7573 24.2646 22.3372 24.2731C21.9171 24.2816 21.51 24.1271 21.2013 23.8421L14.9992 17.64L8.79706 23.8421C8.64841 24.0029 8.46881 24.132 8.26904 24.2217C8.06926 24.3114 7.85343 24.3598 7.63449 24.3641C7.41554 24.3683 7.198 24.3283 6.99489 24.2465C6.79178 24.1646 6.6073 24.0425 6.4525 23.8876C6.29771 23.7327 6.1758 23.5482 6.09407 23.345C6.01234 23.1418 5.97248 22.9243 5.97689 22.7053C5.9813 22.4864 6.02988 22.2706 6.11971 22.0709C6.20955 21.8712 6.33879 21.6917 6.4997 21.5431L12.7018 15.341L6.4997 9.14206C6.33879 8.99351 6.20955 8.814 6.11971 8.61429C6.02988 8.41458 5.9813 8.19879 5.97689 7.97984C5.97248 7.7609 6.01234 7.54333 6.09407 7.34016C6.1758 7.137 6.29771 6.95243 6.4525 6.79753C6.6073 6.64263 6.79178 6.52059 6.99489 6.43872C7.198 6.35686 7.41554 6.31685 7.63449 6.32111C7.85343 6.32536 8.06926 6.37379 8.26904 6.46349C8.46881 6.55319 8.64841 6.68231 8.79706 6.84311L14.9992 13.0436L21.2013 6.84153C21.51 6.55651 21.9171 6.40204 22.3372 6.41049C22.7573 6.41895 23.1578 6.58967 23.4548 6.88689C23.7518 7.18411 23.9223 7.58476 23.9305 8.00487C23.9386 8.42498 23.7839 8.83194 23.4986 9.14048L17.2965 15.341L23.4986 21.5431Z" fill="black"/>
					</svg>
				</div>
			</div>
		</div>
	)
}

export default FolderItem