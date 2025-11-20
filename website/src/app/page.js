export default function Home() {
  return (
    <main className="container mt-5" style={{ maxWidth: 600 }}>
      <h1 className="text-center mb-4">🌅 Sunrise Alarm</h1>

      <p className="text-center text-muted mb-4">
        Manage alarms and device settings.
      </p>

      <div className="d-grid gap-3">
        <a href="/settings" className="btn btn-primary btn-lg">
          ⏰ Manage Alarms
        </a>
      </div>
    </main>
  );
}

