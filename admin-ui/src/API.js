import axios from 'axios';

export const getMembersData = (callback) => {
    axios
    .get(process.env.REACT_APP_MEMBER_DATA_API_URL)
    .then(resp => {
            callback(resp)
        }
    )
    .catch(error => console.log('get error', error));
    
    // return resp;
}