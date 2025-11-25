"use client";

import { useState, useEffect } from "react";

export default function SettingsPage() {
  const [settings, setSettings] = useState({
    volume: 50,
    brightness: 50
  });

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  // Load settings on page load
  useEffect(() => {
    async function load() {
      const res = await fetch("/api/settings");
      const data = await res.json();
      setSettings(data);
      setLoading(false);
    }
    load();
  }, []);

  // Save settings
  async function saveSettings() {
    setSaving(true);

    const res = await fetch("/api/settings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(settings),
    });

    const updated = await res.json();
    setSettings(updated);

    setSaving(false);
    alert("Settings saved!");
  }

  if (loading) return <p className="container mt-5">Loading...</p>;

  return (
    <main className="container mt-5" style={{ maxWidth: 600 }}>
        <h1 className="mb-4">Settings</h1>

      {/* Volume */}
      <div className="mb-4">
        <label className="form-label">
          Volume: <strong>{settings.volume}</strong>
        </label>
        <input
          type="range"
          className="form-range"
          min="0"
          max="100"
          value={settings.volume}
          onChange={(e) =>
            setSettings({ ...settings, volume: parseInt(e.target.value) })
          }
        />
      </div>

      {/* Brightness */}
      <div className="mb-4">
        <label className="form-label">
          Brightness: <strong>{settings.brightness}</strong>
        </label>
        <input
          type="range"
          className="form-range"
          min="0"
          max="100"
          value={settings.brightness}
          onChange={(e) =>
            setSettings({ ...settings, brightness: parseInt(e.target.value) })
          }
        />
      </div>

      <button
        className="btn btn-primary"
        onClick={saveSettings}
        disabled={saving}
      >
        {saving ? "Saving..." : "Save Settings"}
      </button>
    </main>
  );
}

