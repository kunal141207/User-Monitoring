import {GET_EDGES} from '../actions/types.js';

const initialState ={
    edges: []
}

export default function(state= initialState, action){
    switch(action.type){
        case GET_EDGES:
            return{
                ...state,
                edges: action.payload
            }
        default:
            return state;
            
    }
}