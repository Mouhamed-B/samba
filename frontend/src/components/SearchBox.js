import React from 'react';
import './form';
export default class SearchBox extends Component {
    constructor(props){
        super(props)
        this.state = {
            search:props.search
        }
    }
    render() {
        return (
            <div id="search-box" className="row py-3 mb-3 radius">
                <div className="col-12 col-md-2 br-s-1 ">
                    <h4 align='center'>Effectuer une recherche</h4>
                </div>
                <form className="col-12 col-md-8 br-s-1 px-4">
                    <div className="input-group flex-nowrap">
                        <div className="input-group-prepend d-none d-sm-flex">
                            <button type="button" className="btn btn-outline-secondary dropdown-toggle bg-blue" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Action</button>
                            <div className="dropdown-menu">
                                <a className="dropdown-item" href="#">Action</a>
                                <a className="dropdown-item" href="#">Another action</a>
                                <a className="dropdown-item" href="#">Something else here</a>
                                <div role="separator" className="dropdown-divider"></div>
                                <a className="dropdown-item" href="#">Separated link</a>
                            </div>
                        </div>
                        <TextField name/>
                        <div className="input-group-append">
                            <button className="btn bg-blue" type="button"><i className="fas fa-search"></i></button>
                        </div>
                    </div>
                </form>
            </div>
            
            )
        }
    }
    