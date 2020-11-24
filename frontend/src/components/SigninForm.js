import React from 'react'

import React, { Component } from 'react'

export default class SigninForm extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email:  props.email,
            password: props.password,
        }
        this.handleChange = this.handleChange.bind(this)
    }
    handleChange(e){
        const name = e.target.name
        const type = e.target.type
        const value = type === 'checkbox' ? e.target.checked : e.target.value
        this.setState({
            [name] : value
        })
    }
    render() {
        return 
        <form>
            <EmailField onChange={this.handleChange} value={this.state.email}/>
            <PasswordField onChange={this.handleChange} value={this.state.password}/>
        </form>
    }
}

SigninForm.defaultProps = {
    email:null,
    password: null,
}