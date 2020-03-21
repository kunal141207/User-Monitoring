import axios from 'axios';
import {GET_EDGES} from './types';

//Get edges
export const getEdges = () => dispatch => {
     axios.get('/api/edges/')
        .then(res=>{
          dispatch({
              type: GET_EDGES,
              payload: res.data
          });  
        }).catch(err=>console.log(err));
}