import { promises as fs } from "fs";
import path from "path";

const FILE = path.join(process.cwd(), "data", "settings.json");

// Read settings
async function readSettings() {
  try {
    const data = await fs.readFile(FILE, "utf-8");
    return JSON.parse(data);
  } catch {
    // default values if file doesn't exist
    return {
      volume: 50,
      brightness: 50
    };
  }
}

// Write settings
async function writeSettings(settings) {
  await fs.mkdir(path.dirname(FILE), { recursive: true });
  await fs.writeFile(FILE, JSON.stringify(settings, null, 2));
}

// GET /api/settings
export async function GET() {
  const settings = await readSettings();
  return Response.json(settings);
}

// POST /api/settings
export async function POST(req) {
  const newSettings = await req.json();
  const currentSettings = await readSettings();

  // merge old + new
  const updated = { ...currentSettings, ...newSettings };

  await writeSettings(updated);

  return Response.json(updated);
}

