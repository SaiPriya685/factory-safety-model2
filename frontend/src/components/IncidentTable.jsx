import {useEffect,useState} from "react";

import api from "../services/api";


function IncidentTable(){


const [incidents,setIncidents]=useState([]);



useEffect(()=>{


const loadIncidents=async()=>{


const res =
await api.get(
"/incidents/latest"
);


setIncidents(res.data);


};


loadIncidents();


const interval =
setInterval(
loadIncidents,
5000
);


return ()=>clearInterval(interval);



},[]);




const generateReport = async(id)=>{


try{


const response =
await api.get(
`/reports/${id}`,
{
    responseType:"blob"
}
);



const file =
new Blob(
[response.data],
{
type:"application/pdf"
}
);



const url =
window.URL.createObjectURL(
file
);



const link =
document.createElement("a");


link.href=url;


link.download =
`incident_${id}.pdf`;


document.body.appendChild(link);


link.click();


link.remove();



}
catch(error){

console.log(error);

alert(
"Report generation failed"
);

}


};




return(


<div className="incident-table">


<h2>
📋 Recent Safety Incidents
</h2>



<table>


<thead>

<tr>

<th>
Time
</th>


<th>
Violation
</th>


<th>
Severity
</th>


<th>
Location
</th>


<th>
Report
</th>


</tr>


</thead>




<tbody>


{
incidents.map(
(item)=>(


<tr key={item.id}>


<td>

{
new Date(
item.created_at
)
.toLocaleTimeString()
}

</td>



<td>
{item.violation}
</td>



<td className={item.severity}>
{item.severity}
</td>



<td>
{item.location}
</td>



<td>


<button

onClick={()=>
generateReport(item.id)
}

>

📄 Generate Report

</button>


</td>



</tr>


)

)

}



</tbody>


</table>



</div>


)


}


export default IncidentTable;