import React from 'react';
import Badge from '../Badge';

const LeaderboardTable = ({ data }) => {
  return (
    <div className="max-w-4xl mx-auto p-6 bg-gray-800 text-white rounded-lg shadow-lg">
      <h2 className="text-3xl font-bold mb-6 text-center">Leaderboard</h2>
      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-900">
            <th className="border border-gray-700 py-2">Rank</th>
            <th className="border border-gray-700 py-2">Player</th>
            <th className="border border-gray-700 py-2">Badge</th>
            <th className="border border-gray-700 py-2">Score</th>
          </tr>
        </thead>
        <tbody>
          {data.map((player, index) => (
            <tr key={player.id} className="odd:bg-gray-700 even:bg-gray-600">
              <td className="border border-gray-700 py-2 text-center">{index + 1}</td>
              <td className="border border-gray-700 py-2">{player.name}</td>
              <td className="border border-gray-700 py-2 text-center">
                <Badge level={player.badgeLevel} />
              </td>
              <td className="border border-gray-700 py-2 text-center">{player.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LeaderboardTable;
