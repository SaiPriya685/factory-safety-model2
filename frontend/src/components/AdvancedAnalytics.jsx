import { useEffect, useState } from "react";
import api from "../services/api";

import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    Legend,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid
} from "recharts";


function AdvancedAnalytics(){


const [data,setData]=useState(null);



useEffect(()=>{


const loadAnalytics = async()=>{

    const res = await api.get(
        "/advanced/summary"
    );

    setData(res.data);

};


loadAnalytics();


},[]);



if(!data)
return <h3>Loading Analytics...</h3>;



const violationData =
Object.keys(data.violations).map(
(key)=>({

name:key,

value:data.violations[key]

})
);



const severityData =
Object.keys(data.severity).map(
(key)=>({

name:key,

count:data.severity[key]

})
);



return(

<div className="analytics">


<h2>
📊 Advanced Safety Analytics
</h2>



<div className="charts">


<div className="chart-card">


<h3>
Violation Distribution
</h3>


<PieChart width={350} height={300}>


<Pie

data={violationData}

dataKey="value"

nameKey="name"

outerRadius={100}

label

>


{
violationData.map(
(entry,index)=>(

<Cell key={index}/>

)

)
}


</Pie>


<Tooltip/>

<Legend/>


</PieChart>


</div>





<div className="chart-card">


<h3>
Severity Analysis
</h3>


<BarChart

width={400}

height={300}

data={severityData}

>


<CartesianGrid strokeDasharray="3 3"/>


<XAxis dataKey="name"/>


<YAxis/>


<Tooltip/>


<Bar

dataKey="count"

/>


</BarChart>


</div>


</div>


</div>

);


}


export default AdvancedAnalytics;