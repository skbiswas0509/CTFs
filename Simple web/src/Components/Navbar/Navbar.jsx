import React from 'react'
import logo from '../../assets/vite.svg'
import './Navbar.css'

function Navbar() {
  return (

    <div className='Navbar'>
        <div>
            <img className='logo' src={logo} alt="Logo here" />
        </div>
        <div className='item-box'>
            <div className='items'>
                <p>About</p>
                <p>Hero</p>
                <p>Form</p>
            </div>
        </div>
    </div>

  )
}

export default Navbar