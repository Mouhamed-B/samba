import React from 'react';
import './form'


class SignupForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            first_name: props.first_name,
            last_name: props.last_name,
            username: props.username,
            email:  props.email,
            password: props.password,
            is_superuser: props.is_superuser
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
        return <div className='container mt-5'>
        <form className='w-50'>
        <TextField onChange={this.handleChange} value={this.state.first_name} name='first_name'>Prénom</TextField>
        <TextField onChange={this.handleChange} value={this.state.last_name} name='last_name'>Nom</TextField>
        <TextField onChange={this.handleChange} value={this.state.username} name='username'>Nom d'utilisateur</TextField>
        <EmailField onChange={this.handleChange} value={this.state.email}/>
        <PasswordField onChange={this.handleChange} value={this.state.password}/>
        <CheckboxField onChange={this.handleChange} value={this.state.is_superuser} name='is_superuser'>Est superutilisateur</CheckboxField>
        </form>
        </div>
    }
    
}
SignupForm.defaultProps = {
    first_name:null,
    last_name:null,
    username:null, 
    email:null,
    password: null,
    is_superuser: null,
}