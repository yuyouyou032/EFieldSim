const BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

export async function fetchScene(params) {
  const res = await fetch(`${BASE}/api/update`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params)
  });
  if (!res.ok) throw new Error(`backend ${res.status}`);
  return res.json(); // expect { rays: [...], meta: {...} }
}