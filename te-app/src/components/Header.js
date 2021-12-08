import PropTypes from 'prop-types'
import TheButton from "./Button"
import {useEffect, useState} from 'react'

const Header = ({title,onAdd,showAdd}) =>{
    const [totalStocks, setTotalStocks] = useState([])

    useEffect(() => {
        getTotalStocks()
    },[])

    const getTotalStocks = async () => {
        //Cannon do https since server is not configured for it
        const response = await fetch("http://localhost:8000/getTotalStocks")
        const stocks = await response.json()
        console.log(stocks)
        setTotalStocks(stocks.totalStocks)
      }

    return (
        <header>
            <h1>{title} {totalStocks}</h1>
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