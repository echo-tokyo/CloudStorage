import { useState } from 'react'
import { createGlobalStyle } from 'styled-components';
import {setIsClicked} from './'

function Themes () {
    export const [isClicked, setIsClicked] = useState(() => {
        const savedTheme = localStorage.getItem('isBlackTheme');
        return savedTheme ? savedTheme === 'true' : false; // используем сохраненное значение, если оно существует
    })
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
        <GlobalStyles isClicked={isClicked}/>
    )
}

export default Themes