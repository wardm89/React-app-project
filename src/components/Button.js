import PropTypes from 'prop-types'
import {Button} from 'semantic-ui-react'



const TheButton = ({color, text, onClick}) => {

    return (
        <button onClick={onClick} style={{
            backgroundColor: color}} className='btn'>
            {text}
        </button>
    )
}


Button.defaultProps = {
    color: 'steelblue',
}

Button.prototypes = {
    text: PropTypes.string,
    color: PropTypes.string,
    onClick: PropTypes.func.isRequired,
}

export default TheButton

