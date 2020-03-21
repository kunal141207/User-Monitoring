import axios from 'axios';
import {GET_IMAGES} from './types';

//Get images
export const getImages = () => dispatch => {
     axios.get('/api/images/')
        .then(res=>{
          dispatch({
              type: GET_IMAGES,
              payload: res.data
          });  
        }).catch(err=>console.log(err));
}