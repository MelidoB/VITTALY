import React, { useEffect } from "react";
import { Toaster, toast } from "sonner";
import { RecentEntries, ScanFood, TodaysSummary } from "../components/cards/DashboardCards";
import Header from "../components/Header";

// Main menu page (Dashboard)
function Dashboard() {

    //// Welcome message logic ////
    // List of welcome messages
    const welcomeMessages = [
        "Welcome back!",
        "Ready to level up your nutrition? Snap, track, and fuel your progress, one meal at a time!",
        "Consistency is key, to achieve your goals!",
        "Let's track it and make it count!",
        "You can start with an easy Snap!",
        "What time it is? it's meal time!",
        "Your training never stops, eat food to gaining exp and level up!",
        "A true warrior never skips disciplined, you got this!"
    ];

    useEffect(() => {
        const hasSeenWelcome = sessionStorage.getItem("welcomeMessageShown");

        // Checks if the welcome message has not been seen
        if (!hasSeenWelcome) {
            // Select a random message
            const randomMessage = welcomeMessages[Math.floor(Math.random() * welcomeMessages.length)];

            toast.success(randomMessage, {
                duration: Infinity, // Keeps it open until clicked
                action: {
                    label: "Got it!",
                    onClick: () => toast.dismiss(), // Dismiss when button is clicked
                },
            });

            sessionStorage.setItem("welcomeMessageShown", "true");
        }
    }, []);
    //// Welcome message logic ////

    return (
        <div className="min-h-screen bg-gray-100">
      <Header />
        <div className="dashboard">
            <Toaster position="top-right" richColors />
            <TodaysSummary />
            <ScanFood />
            <RecentEntries />
        </div>
    </div>
    );
}

export default Dashboard;
