export default function Home() {
  return (
    <main className="container mt-5" style={{ maxWidth: 600 }}>
      <h1 className="text-center mb-4"> Sunrise Alarm</h1>


      <div className="d-grid gap-3">
        <a href="/alarms" className="mb-4 btn btn-primary btn-lg">
           Manage Alarms
        </a>
        <a href="/settings" className="btn btn-primary btn-lg">
           Manage Settings
        </a>
      </div>
    </main>
  );
}

