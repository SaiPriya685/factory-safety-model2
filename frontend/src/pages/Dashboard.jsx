import Navbar from "../components/Navbar";
import {useEffect,useState} from "react";
import CameraFeed from "../components/CameraFeed";
import api from "../services/api";

import StatCard from "../components/StatCard";

import "../styles/dashboard.css";
import IncidentTable from "../components/IncidentTable";
import LiveMonitor from "../components/LiveMonitor";
import AnalyticsCharts from "../components/AnalyticsCharts";
import AdvancedAnalytics from "../components/AdvancedAnalytics";
import CameraControl from "../components/CameraControl";
function Dashboard(){


const [stats,setStats]=useState(null);



useEffect(()=>{

loadStats();

},[]);



const loadStats=async()=>{

const res =
await api.get(
"/dashboard/stats"
);


setStats(res.data);

};



if(!stats)
return <h2>Loading...</h2>



return(
<>

<Navbar />
<div className="dashboard">


<h1 className="title">
AI Factory Safety Dashboard
</h1>


<div className="cards">


<StatCard
title="Total Incidents"
value={stats.total_incidents}
icon="📋"
/>


<StatCard
title="Fire Emergencies"
value={stats.critical_events}
icon="🔥"
/>


<StatCard
title="Fire Events"
value={stats.fire_events}
icon="🚨"
/>


<StatCard
title="Helmet Violations"
value={stats.helmet_violations}
icon="⛑️"
/>


</div>


<StatCard
    title="Safety Score"
    value={`${stats.safety_score}%`}
    icon="🛡️"
/>
<CameraControl />
<CameraFeed />
<LiveMonitor/>
<IncidentTable/>
<AnalyticsCharts stats={stats} />
<AdvancedAnalytics />
</div>
</>
)


}


export default Dashboard;