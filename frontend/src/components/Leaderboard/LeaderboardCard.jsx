import React from 'react';

const LeaderboardCard = ({ player, rank }) => {
  return (
    <div className="bg-gray-800 text-white rounded-lg shadow-md p-4 m-2 flex items-center">
      <div className="text-3xl font-bold mr-4">{rank}</div>
      <div>
        <div className="text-xl font-semibold">{player.name}</div>
        <div className="text-sm text-gray-400">Score: {player.score}</div>
      </div>
    </div>
  );
};

export default LeaderboardCard;
