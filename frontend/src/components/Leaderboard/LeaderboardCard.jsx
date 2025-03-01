import React from 'react';
import Badge from '../Badge';

const LeaderboardCard = ({ player, rank }) => {
  return (
    <div className="bg-gray-800 text-white rounded-lg shadow-lg p-4 m-4 flex items-center">
      <div className="text-4xl font-bold mr-6">{rank}</div>
      <div className="flex flex-col">
        <div className="text-2xl font-semibold">{player.name}</div>
        <div className="mt-2">
          <Badge level={player.badgeLevel} />
        </div>
        <div className="text-lg text-gray-400 mt-1">Score: {player.score}</div>
      </div>
    </div>
  );
};

export default LeaderboardCard;
