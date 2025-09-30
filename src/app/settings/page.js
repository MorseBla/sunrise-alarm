"use client";

import { useState, useEffect } from "react";

export default function SettingsPage() {
  const [time, setTime] = useState("");

  // Load existing alarm from backend
  useEffect(() => {
    fetch("/api/alarm")
      .then(res => res.json())
      .then(data => {
        if (data.time) setTime(data.time);
      });
  }, []);

  // Save new alarm
  async function handleSave(e) {
    e.preventDefault();
    await fetch("/api/alarm", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ time }),
    });
    alert("Alarm saved!");
  }

  return (
    <main className="container mt-5">
      <h1>⏰ Alarm Settings</h1>
      <form onSubmit={handleSave} className="mt-3">
        <label className="form-label">Alarm Time:</label>
        <input
          type="time"
          className="form-control"
          value={time}
          onChange={(e) => setTime(e.target.value)}
        />
        <button type="submit" className="btn btn-primary mt-3">
          Save
        </button>
      </form>
    </main>
  );
}

