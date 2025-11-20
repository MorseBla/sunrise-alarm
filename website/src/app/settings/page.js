"use client";

import { useState, useEffect } from "react";

export default function SettingsPage() {
  const [alarms, setAlarms] = useState([]);
  const [newTime, setNewTime] = useState("");
  const [loading, setLoading] = useState(true);

  // Load alarms on mount
  useEffect(() => {
    async function load() {
      const res = await fetch("/api/alarms");
      const data = await res.json();
      setAlarms(data);
      setLoading(false);
    }
    load();
  }, []);

  // Add an alarm
  async function addAlarm() {
    if (!newTime) return;

    const res = await fetch("/api/alarms", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ time: newTime })
    });

    const alarm = await res.json();
    setAlarms([...alarms, alarm]);
    setNewTime("");
  }

  // Toggle enable/disable
  async function toggleAlarm(alarm) {
    await fetch("/api/alarms", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: alarm.id,
        enabled: !alarm.enabled
      })
    });

    setAlarms(
      alarms.map((a) =>
        a.id === alarm.id ? { ...a, enabled: !a.enabled } : a
      )
    );
  }

  // Delete an alarm
  async function deleteAlarm(alarm) {
    await fetch("/api/alarms", {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: alarm.id })
    });

    setAlarms(alarms.filter((a) => a.id !== alarm.id));
  }

  if (loading) return <p className="container mt-5">Loading...</p>;

  return (
    <main className="container mt-5" style={{ maxWidth: 600 }}>
      <h1 className="mb-4">⏰ Alarm Settings</h1>

      {/* Add new alarm */}
      <div className="input-group mb-4">
        <input
          type="time"
          className="form-control"
          value={newTime}
          onChange={(e) => setNewTime(e.target.value)}
        />
        <button className="btn btn-success" onClick={addAlarm}>
          Add
        </button>
      </div>

      {/* List alarms */}
      <ul className="list-group">
        {alarms.map((alarm) => (
          <li
            key={alarm.id}
            className="list-group-item d-flex justify-content-between align-items-center"
          >
            <span>{alarm.time}</span>

            {/* Toggle switch */}
            <label className="switch">
              <input
                type="checkbox"
                checked={alarm.enabled}
                onChange={() => toggleAlarm(alarm)}
              />
              <span className="slider"></span>
            </label>

            <button
              className="btn btn-sm btn-danger"
              onClick={() => deleteAlarm(alarm)}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </main>
  );
}

