import React from 'react'
import './Form.css'

export default function Form() {
  return (
    <div className='container'>
        <div className='title'>Contact Form</div>
        <div className='infos'>
            <p className='name-info'>Name</p>
            <input type="text" className='name-field' />
            <p className='email-info'>Email</p>
            <input type="text" className='email-field' />
            <p className='phone-info'>Phone</p>
            <input type="text" className='phone-field' placeholder='(+880)'/>
        </div>
        <div className='Message'>
            <p className='message-text'>Your message</p>
            <input type="text" className='message-field' />
        </div>
    </div>
  )
}
