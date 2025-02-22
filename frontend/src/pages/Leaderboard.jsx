import React from 'react';
import LeaderboardTable from '../components/Leaderboard/LeaderboardTable';

const Leaderboard = () => {
  // Placeholder data for the leaderboard
  const sampleData = [
    { id: 1, name: 'Alice', score: 1500 },
    { id: 2, name: 'Bob', score: 1200 },
    { id: 3, name: 'Charlie', score: 900 },
  ];

  return (
    <div className="container mx-auto p-4">
      <LeaderboardTable data={sampleData} />
    </div>
  );
};

export default Leaderboard;
