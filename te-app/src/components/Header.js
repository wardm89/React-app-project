import PropTypes from 'prop-types'
import TheButton from "./Button";


const Header = ({title,onAdd,showAdd}) =>{

    return (
        <header>
            <h1>{title}</h1>
            <TheButton text={showAdd ? 'Hide Form' : 'Add Task'} color={showAdd ? 'Red' : 'Green'} onClick={onAdd}/>
        </header>
    )
}

Header.defaultProps = {
    title: 'Default Title',
}

Header.propTypes ={
    title: PropTypes.string.isRequired,

}


export default Header