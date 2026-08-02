import { useEffect, useState, useRef } from "react";
import api from "../services/api";
import { toast } from "react-toastify";

function LiveMonitor() {

    const [data, setData] = useState(null);

    // Stores last alert to avoid duplicate notifications
    const previousAlert = useRef("");



    // Poll backend every 3 seconds
    useEffect(() => {

        const fetchData = async () => {

            try {

                const res = await api.get("/analytics/live");

                console.log("LIVE DATA:", res.data);

                setData(res.data);

            } 
            catch(error) {

                console.error(
                    "Live monitor error:",
                    error
                );

            }

        };


        fetchData();


        const interval = setInterval(
            fetchData,
            3000
        );


        return () => clearInterval(interval);


    }, []);




    // Emergency alert popup
    useEffect(() => {


        if (!data)
            return;


        if (data.risk_level !== "CRITICAL")
            return;



        const currentAlert = data.violations
            .map(v => v.type)
            .join(",");



        // Avoid duplicate popup
        if(currentAlert === previousAlert.current)
            return;



        previousAlert.current = currentAlert;



        toast.error(

            <>

                <strong>
                    🚨 EMERGENCY ALERT
                </strong>


                <br />
                <br />


                <b>
                    Risk Level: CRITICAL
                </b>


                <br />
                <br />


                {
                    data.violations.map(
                        (v,index)=>(

                        <div key={index}>

                            🔴 {v.type}

                            <br />

                            Severity:
                            {" "}
                            {v.severity}

                            <br />

                            Confidence:
                            {" "}
                            {(v.confidence * 100).toFixed(1)}%

                            <br />
                            <br />

                        </div>

                    ))
                }


                ⚠️ Immediate action required!


            </>,


            {

                autoClose:8000,

                position:"top-right"

            }


        );


    },[data]);





    if(!data)

        return (
            <h3>
                Loading AI Monitor...
            </h3>
        );





    return (

        <div className="live-monitor">


            <h2>
                🎥 Live AI Safety Monitor
            </h2>




            <h1>

                Risk Level:


                <span 
                className={`risk-badge ${data.risk_level}`}>

                    {data.risk_level}

                </span>


            </h1>





            <h3>
                🚨 Active Violations
            </h3>





            {
                !data.violations || 
                data.violations.length === 0 ? (

                    <p>
                        No active violations.
                    </p>


                ) : (


                    data.violations.map(
                        (item,index)=>(


                        <div

                        key={index}

                        className="violation-card"

                        >


                            <p>

                                {item.type}

                            </p>



                            <p>

                                Severity:
                                {" "}
                                {item.severity}

                            </p>



                            <p>

                                Confidence:
                                {" "}
                                {(item.confidence * 100).toFixed(1)}%

                            </p>



                        </div>


                    ))

                )

            }



        </div>


    );

}


export default LiveMonitor;