import {useState} from "react";
import {useNavigate} from "react-router-dom";

import api from "../services/api";


function Signup(){

const navigate = useNavigate();


const [name,setName]=useState("");
const [email,setEmail]=useState("");
const [password,setPassword]=useState("");



const signup = async()=>{


try{


await api.post(
"/auth/register",
{
name,
email,
password
}
);


alert(
"Registration successful. Please login."
);


navigate("/");


}

catch(error){

console.log(error);

alert(
"Signup failed"
);

}


}



return(

<div>


<h1>
AI Factory Safety Copilot
</h1>


<h2>
Create Account
</h2>



<input
placeholder="Name"
value={name}
onChange={
e=>setName(e.target.value)
}
/>



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



<button onClick={signup}>
Register
</button>


<p>

Already have account?

<button
onClick={()=>navigate("/")}
>
Login
</button>


</p>


</div>

)


}


export default Signup;