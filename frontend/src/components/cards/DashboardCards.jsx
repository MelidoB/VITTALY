import React from "react";

// TodaysSummary Component
function TodaysSummary() {
    const progress1 = 75;
    return(
            <div className="card">
                <h2>Today's Summary</h2>
                <h3>MacroNutrients: </h3>
                <p>Calories Consumed: <strong>0 kcal</strong></p>
                <p>Protein Consumed: <strong>0</strong></p>
                <p>Carbs Consumed: <strong>0</strong></p>
                <p>Fats Consumed: <strong>0</strong></p>
                <p>Fiber Consumed: <strong>0</strong></p>

                <h3>MicroNutrients: </h3>
                <p>TBD</p>

                <p>Goal: <strong>TBD</strong></p>
            </div>
    ); 
}

// ScanFood Component
function ScanFood() {
    return(
        <div className="card">
            <h2>Scan Food</h2>
            <button>Upload or Take a picture</button>
        </div>
    );
}

// RecentEntries Component
function RecentEntries() {
    return (
        <div className="card">
            <h2>Recent Entries</h2>
            <ul>
                <li>No recent entries</li>
            </ul>
        </div>
    );
}

export { TodaysSummary, ScanFood, RecentEntries};
