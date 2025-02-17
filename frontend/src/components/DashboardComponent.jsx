import React from "react";
import DropdownButton from "./DropDownButtonComponent";

// ScanFood Component
function ScanFood() {
  return (
    <div className="item">
      <button>
        <h3>Scan Food</h3>
      </button>
    </div>
  );
}

// TodaysSummary Component
function TodaysSummary() {
  const todaysSummaryApiCall = {
    calories: 2000,
    protein: 140,
    carbs: 360,
    fats: 90,
    fiber: 30,
    vitamin_a: 1,
    vitamin_c: 1,
    vitamin_d: 1,
    vitamin_e: 1,
    vitamin_k: 1,
    vitamin_b1: 1,
    vitamin_b2: 1,
    vitamin_b3: 1,
    vitamin_b6: 1,
    vitamin_b9: 1,
    vitamin_b12: 1,
  };

  return (
    <div className="item">
      <h2>Today's Summary</h2>
      <p>
        [ Calories ]: <strong>0 / {todaysSummaryApiCall.calories} kcal</strong>
      </p>
      <p>
        [ Protein ]: <strong>0 / {todaysSummaryApiCall.protein} g</strong>
      </p>
      <p>
        [ Carbs ]: <strong>0 / {todaysSummaryApiCall.carbs} g</strong>
      </p>
      <p>
        [ Fats ]: <strong>0 / {todaysSummaryApiCall.fats} g</strong>
      </p>
      <p>
        [ Fiber ]: <strong>0 / {todaysSummaryApiCall.fiber} g</strong>
      </p>

      <DropdownButton buttonText="More Nutrients">
        <h2>Extra: MicroNutrients</h2>

        <h4>Vitamins:</h4>
        <p>
          [ Vitamin A ]: <strong>0 / {todaysSummaryApiCall.vitamin_a} µg</strong>
        </p>
        <p>
          [ Vitamin C ]: <strong>0 / {todaysSummaryApiCall.vitamin_c} mg</strong>
        </p>
        <p>
          [ Vitamin D ]: <strong>0 / {todaysSummaryApiCall.vitamin_d} µg</strong>
        </p>
        <p>
          [ Vitamin E ]: <strong>0 / {todaysSummaryApiCall.vitamin_e} mg</strong>
        </p>
        <p>
          [ Vitamin K ]: <strong>0 / {todaysSummaryApiCall.vitamin_k} µg</strong>
        </p>
        <p>
          [ Vitamin B1 (Thiamine) ]:{" "}
          <strong>0 / {todaysSummaryApiCall.vitamin_b1} mg</strong>
        </p>
        <p>
          [ Vitamin B2 (Riboflavin) ]:{" "}
          <strong>0 / {todaysSummaryApiCall.vitamin_b2} mg</strong>
        </p>
        <p>
          [ Vitamin B3 (Niacin) ]:{" "}
          <strong>0 / {todaysSummaryApiCall.vitamin_b3} mg</strong>
        </p>
        <p>
          [ Vitamin B6 ]: <strong>0 / {todaysSummaryApiCall.vitamin_b6} mg</strong>
        </p>
        <p>
          [ Vitamin B9 (Folate) ]:{" "}
          <strong>0 / {todaysSummaryApiCall.vitamin_b9} µg</strong>
        </p>
        <p>
          [ Vitamin B12 ]:{" "}
          <strong>0 / {todaysSummaryApiCall.vitamin_b12} µg</strong>
        </p>

        <h4>Minerals:</h4>
        <p>
          [ Calcium ]: <strong>0 / {todaysSummaryApiCall.calcium} mg</strong>
        </p>
        <p>
          [ Iron ]: <strong>0 / {todaysSummaryApiCall.iron} mg</strong>
        </p>
        <p>
          [ Magnesium ]:{" "}
          <strong>0 / {todaysSummaryApiCall.magnesium} mg</strong>
        </p>
        <p>
          [ Potassium ]:{" "}
          <strong>0 / {todaysSummaryApiCall.potassium} mg</strong>
        </p>
        <p>
          [ Sodium ]: <strong>0 / {todaysSummaryApiCall.sodium} mg</strong>
        </p>
        <p>
          [ Zinc ]: <strong>0 / {todaysSummaryApiCall.zinc} mg</strong>
        </p>
      </DropdownButton>
    </div>
  );
}

// RecentEntries Component
function RecentEntries() {
  return (
    <div className="item">
      <h2>Recent Entries</h2>
      <ol>
        <li>No recent entries</li>
      </ol>
    </div>
  );
}

export { RecentEntries, ScanFood, TodaysSummary };

