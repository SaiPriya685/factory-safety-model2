import axios from "axios";


const api = axios.create({

    baseURL: "https://factory-safety-model2.onrender.com",

    headers:{
        "Content-Type":"application/json"
    }

});


export default api;