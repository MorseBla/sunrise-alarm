import { promises as fs } from "fs";

const SETTINGS_FILE = "alarm.json";

// GET /api/alarm → returns current alarm
export async function GET() {
  try {
    const data = await fs.readFile(SETTINGS_FILE, "utf-8");
    return Response.json(JSON.parse(data));
  } catch (err) {
    // If file doesn't exist yet
    return Response.json({ time: null });
  }
}

// POST /api/alarm → save new alarm
export async function POST(req) {
  const body = await req.json();
  await fs.writeFile(SETTINGS_FILE, JSON.stringify(body, null, 2));
  return Response.json({ message: "Alarm saved!" });
}

