import React from "react";
import ScanFood from "./ScanFoodComponent";
import TodaysSummary from "./TodaysSummaryComponent";
import RecentEntries from "./RecentEntriesComponent";


function DashboardComponent() {

  return (
    <div className="min-h-screen bg-background text-primary">
      <ScanFood />
      <TodaysSummary />
      <RecentEntries />
    </div>
  );
}

export default DashboardComponent;
