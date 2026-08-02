function StatCard({title,value,icon}){


return(

<div className="stat-card">

<h3>
{icon} {title}
</h3>

<h1 className="score-value">
{value}
</h1>

</div>

)

}


export default StatCard;