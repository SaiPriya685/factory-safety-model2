import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    ResponsiveContainer
} from "recharts";

function AnalyticsCharts({ stats }) {

    const pieData = [
        {
            name: "Fire",
            value: stats.fire_events
        },
        {
            name: "Helmet",
            value: stats.helmet_violations
        }
    ];

    const barData = [
        {
            name: "Critical",
            value: stats.critical_events
        },
        {
            name: "High",
            value: stats.high_risk_events
        }
    ];

    const COLORS = ["#ef4444", "#3b82f6"];

    return (

        <div className="charts">

            <div className="chart-card">

                <h2>Fire vs Helmet Violations</h2>

                <ResponsiveContainer width="100%" height={300}>

                    <PieChart>

                        <Pie
                            data={pieData}
                            dataKey="value"
                            outerRadius={100}
                        >

                            {
                                pieData.map((entry, index) => (
                                    <Cell
                                        key={index}
                                        fill={COLORS[index]}
                                    />
                                ))
                            }

                        </Pie>

                        <Tooltip />

                    </PieChart>

                </ResponsiveContainer>

            </div>

            <div className="chart-card">

                <h2>Risk Distribution</h2>

                <ResponsiveContainer width="100%" height={300}>

                    <BarChart data={barData}>

                        <CartesianGrid strokeDasharray="3 3" />

                        <XAxis dataKey="name" />

                        <YAxis />

                        <Tooltip />

                        <Bar dataKey="value" fill="#2563eb" />

                    </BarChart>

                </ResponsiveContainer>

            </div>

        </div>

    );

}

export default AnalyticsCharts;