import React from 'react';
import badge1 from '../assets/badges/badge_1.png';
import badge2 from '../assets/badges/badge_2.png';
import badge3 from '../assets/badges/badge_3.png';
import badge4 from '../assets/badges/badge_4.png';
import badge5 from '../assets/badges/badge_5.png';
import badge6 from '../assets/badges/badge_6.png';

const badgeMap = {
  1: badge1,
  2: badge2,
  3: badge3,
  4: badge4,
  5: badge5,
  6: badge6,
};

const Badge = ({ level }) => {
  const badgeImage = badgeMap[level];
  if (!badgeImage) return null;
  return <img src={badgeImage} alt={`Badge ${level}`} className="w-12 h-12" />;
};

export default Badge;
