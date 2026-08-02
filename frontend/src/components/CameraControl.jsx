import { useState, useEffect } from "react";
import api from "../services/api";


function CameraControl(){


const [status,setStatus]=useState(false);



const checkStatus = async()=>{

    try{

        const res =
        await api.get(
            "/camera/status"
        );


        setStatus(
            res.data.running
        );


    }
    catch(error){

        console.log(error);

    }

};



useEffect(()=>{


    checkStatus();


    const interval =
    setInterval(
        checkStatus,
        3000
    );


    return ()=>clearInterval(interval);


},[]);




const startCamera = async()=>{


    try{

        await api.post(
            "/camera/start"
        );


        checkStatus();


    }
    catch(error){

        console.log(error);

    }


};




const stopCamera = async()=>{


    try{

        await api.post(
            "/camera/stop"
        );


        checkStatus();


    }
    catch(error){

        console.log(error);

    }


};




return(

<div className="camera-control">


<h3>
🎥 Camera Control
</h3>



<button

onClick={startCamera}

disabled={status}

>

▶ Start Monitoring

</button>



<button

onClick={stopCamera}

disabled={!status}

>

⏹ Stop Monitoring

</button>




<p>

Status:

{
status
?
"🟢 Running"
:
"🔴 Stopped"
}

</p>



</div>

)

}


export default CameraControl;