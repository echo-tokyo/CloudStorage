import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import filesData from './file.data'
import { useState } from 'react'
import { createGlobalStyle } from 'styled-components';

function FieldItems(){
    const [files, setFile] = useState(filesData)
    
    const [isClicked, setIsClicked] = useState(false)
    const changeTheme = () => {
        setIsClicked(!isClicked)
        localStorage.setItem('isLightTheme', isClicked)
    }
    
    const GlobalStyles = createGlobalStyle`
    body{ 
        background-color: ${props => (props.isClicked ? '#2B2B2B' : 'white')};
    }
    p,a,label{
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    .theme1, .theme2, .theme5{
        stroke:  ${props => (props.isClicked ? 'white' : 'black')};
    }
    .theme3, .theme4{
        fill: ${props => (props.isClicked ? 'white' : 'black')};
    }
    main{
        background-color: ${props => (props.isClicked ? '#383838' : '#DFDFDF')};
    }
    .file-item{
        border-color: ${props => (props.isClicked ? 'white' : 'black')};
    }`

    return(
        <>
        <GlobalStyles isClicked={isClicked}/>
        <Header changeTheme={changeTheme}/>
        <main>
            {files.length ? (
                files.map(file => <FileItem key={file.id} file={file} setFile={setFile} isClicked={isClicked}/>)
            ) : (
                <p>There are no files</p>
            )}
        </main>
        </>
    )
}

export default FieldItems 