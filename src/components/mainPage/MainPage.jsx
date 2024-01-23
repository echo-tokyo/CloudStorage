import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import filesData from './file.data'
import { useState } from 'react'
import Themes from './Themes'

function FieldItems(){
    const [files, setFile] = useState(filesData)
    return(
        <Themes defaultTheme={false}>
            {(changeTheme) => (
                <>
                <Header changeTheme={changeTheme}/>
                <main>
                    {files.length ? (
                        files.map(file => <FileItem key={file.id} file={file} setFile={setFile}/>)
                    ) : (
                        <p>There are no files</p>
                    )}
                </main>
                </>
            )}
        </Themes>
    )
}

export default FieldItems 