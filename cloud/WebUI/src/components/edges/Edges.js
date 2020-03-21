import React, { Component ,Fragment} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import { getEdges} from '../../actions/edges';
import { getImages} from '../../actions/images';               


export class Edges extends Component {
    static PropTypes ={
        edges: PropTypes.array.isRequired,
        images: PropTypes.array.isRequired
    }

    componentDidMount(){
        this.props.getEdges();
        this.props.getImages();
    }

    render() {
        return (
            <Fragment>
                <h1>Edges list</h1>
                {this.props.edges.map(edge=>(
                   <div id={edge.id} class="carousel slide" data-ride="carousel">
                    {this.props.images.map(image=>(<div class="carousel-inner">
                    <div class="carousel-item active">
                        <img class="d-block w-100" src={image.image} alt="First slide"></img>
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Gray_Scale = {image.gray_scale}</h5>
                            <p>Created_at = {image.created_at}</p>
                        </div>
                    </div>                     
                    </div>))}
                   <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                     <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                     <span class="sr-only">Previous</span>
                   </a>
                   <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                     <span class="carousel-control-next-icon" aria-hidden="true"></span>
                     <span class="sr-only">Next</span>
                   </a>
                 </div> 
                ))}
            </Fragment>
        );
    }
}

const mapStateToProps = state =>({
    edges: state.edges.edges,
    images: state.images.images
});

export default connect(mapStateToProps, {getEdges, getImages})(Edges);
