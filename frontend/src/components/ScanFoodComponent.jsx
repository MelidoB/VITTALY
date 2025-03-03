import React, { useState } from "react";

function ScanFood() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadImage = async () => {
    if (!selectedFile) return alert("Select an image to upload.");
    
    setLoading(true);
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("https://vittaly-backend-production.up.railway.app/api/food_recognition", {
        method: "POST",
        body: formData,
    });
    

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ error: "The upload has failed, please try again." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="item scan-food">
      <button onClick={uploadImage} disabled={loading}>
        {loading ? "Scanning..." : "Scan Food"}
      </button>
      <input type="file" accept="image/*" onChange={(e) => setSelectedFile(e.target.files[0])} className="file-input" />

      {result && (
        <div className="result">
          {result.error ? (
            <p style={{ color: "red" }}>{result.error}</p>
          ) : (
            <>
              <h2><b>{"[" + result.food.charAt(0).toUpperCase() + result.food.slice(1) + "]"}</b></h2>
              <p>Calories: {result.calories}</p>
              <p>Protein: {result.macros?.protein}g</p>
              <p>Carbs: {result.macros?.carbs}g</p>
              <p>Fats: {result.macros?.fats}g</p>
              <p>Fiber: {result.macros?.fiber}g</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default ScanFood;