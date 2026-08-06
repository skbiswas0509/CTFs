import React from 'react'
import hero_pic from '../../assets/hero pic.jpg'
import './Hero.css'

export default function Hero() {
    return (
        <div className='hero-container'>
            <div className="hero-left">
                <div>
                    <img className='img' src={hero_pic} alt="" />
                </div>
            </div>
            <div className='hero-right'>
                <p className='text'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis nemo eius sint voluptatibus est eum a quasi rerum labore quos cumque alias, repellendus accusamus incidunt praesentium consequatur laboriosam! Nam, atque.</p>
            </div>
        </div>
    )
}
