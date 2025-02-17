import React, { useEffect } from "react";
import { Toaster, toast } from "sonner";
import { RecentEntries, ScanFood, TodaysSummary } from "../components/DashboardComponent";
import Header from "../components/HeaderComponent";

function Dashboard() {
  const welcomeMessages = [
    "Welcome back!",
    "Ready to level up your nutrition? Snap, track, and fuel your progress, one meal at a time!",
    "Consistency is key to achieve your goals!",
    "Let's track it and make it count!",
    "You can start with an easy Snap!",
    "What time it is? It's meal time!",
    "Your training never stops, eat food to gain exp and level up!",
    "A true warrior never skips discipline, you got this!",
  ];

  useEffect(() => {
    const hasSeenWelcome = sessionStorage.getItem("welcomeMessageShown");
    if (!hasSeenWelcome) {
      const randomMessage = welcomeMessages[Math.floor(Math.random() * welcomeMessages.length)];
      toast.success(randomMessage, {
        duration: Infinity,
        action: {
          label: "Got it!",
          onClick: () => toast.dismiss(),
        },
      });
      sessionStorage.setItem("welcomeMessageShown", "true");
    }
  }, []);

  return (
    <div className="min-h-screen bg-background text-primary">
      <Toaster position="top-right" richColors />
      <Header />
      <div className="dashboard">
        <ScanFood />
        <TodaysSummary />
        <RecentEntries />
      </div>
    </div>
  );
}

export default Dashboard;
