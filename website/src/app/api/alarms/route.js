import { promises as fs } from "fs";
import path from "path";

const FILE = path.join(process.cwd(), "data", "alarms.json");

// Helper: read alarms
async function readAlarms() {
  try {
    const data = await fs.readFile(FILE, "utf-8");
    return JSON.parse(data);
  } catch {
    return []; // file doesn't exist yet
  }
}

// Helper: write alarms
async function writeAlarms(alarms) {
  await fs.mkdir(path.dirname(FILE), { recursive: true });
  await fs.writeFile(FILE, JSON.stringify(alarms, null, 2));
}

// GET /api/alarms → list alarms
export async function GET() {
  const alarms = await readAlarms();
  return Response.json(alarms);
}

// POST /api/alarms → create a new alarm
export async function POST(req) {
  const { time } = await req.json();
  const alarms = await readAlarms();

  const newAlarm = {
    id: Date.now(),
    time,
    enabled: true
  };

  alarms.push(newAlarm);
  await writeAlarms(alarms);

  return Response.json(newAlarm, { status: 201 });
}

// PATCH /api/alarms → update an alarm
export async function PATCH(req) {
  const { id, time, enabled } = await req.json();
  let alarms = await readAlarms();

  alarms = alarms.map((a) =>
    a.id === id ? { ...a, time: time ?? a.time, enabled: enabled ?? a.enabled } : a
  );

  await writeAlarms(alarms);
  return Response.json({ message: "Alarm updated" });
}

// DELETE /api/alarms → delete an alarm
export async function DELETE(req) {
  const { id } = await req.json();
  let alarms = await readAlarms();

  alarms = alarms.filter((a) => a.id !== id);
  await writeAlarms(alarms);

  return Response.json({ message: "Alarm deleted" });
}

