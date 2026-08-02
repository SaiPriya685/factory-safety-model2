import {useState} from "react";
import {useNavigate} from "react-router-dom";

import api from "../services/api";


function Login(){

const navigate = useNavigate();


const [email,setEmail]=useState("");
const [password,setPassword]=useState("");



const login = async()=>{


try{

const response =
await api.post(
"/auth/login",
{
email,
password
}
);


localStorage.setItem(
"token",
response.data.access_token
);


navigate("/dashboard");


}

catch(error){

alert("Login failed");

}


}



return(

<div>

<h1>
AI Factory Safety Copilot
</h1>


<input
placeholder="Email"
value={email}
onChange={
e=>setEmail(e.target.value)
}
/>


<input
type="password"
placeholder="Password"
value={password}
onChange={
e=>setPassword(e.target.value)
}
/>


<button onClick={login}>
Login
</button>


</div>

)


}


export default Login;