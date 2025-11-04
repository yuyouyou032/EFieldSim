```
5cd backend
pip install -r requirements.txt
uvicorn server:app --reload --port 8000

single-cell-sim % curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"amplitude_x":1.0, "amplitude_y":1.7, "frequency":2.58, "phase_diff":0}' \
  http://localhost:8000/api/update
```

**Frontend structure**

```
frontend/
├─ package.json
├─ index.html
├─ vite.config.js            (optional defaults are fine)
└─ src/
   ├─ main.jsx               (entry, mounts React)
   ├─ App.jsx                (top-level app shell)
   ├─ api/
   │  └─ client.js           (HTTP calls to Python backend)
   ├─ components/
   │  ├─ ControlsPanel.jsx   (UI sliders/buttons)
   │  └─ Scene3D.jsx         (three.js canvas + render loop)
   └─ utils/
      └─ convertData.js      (shape data for 3D if needed)
```

**NOTE: app structure**

User moves slider
↓
ControlsPanel calls callback into App.jsx
↓
App.jsx POSTs to backend through api/client.js
↓
Backend returns JSON (points/rays/geometry)
↓
App.jsx updates state
↓
Scene3D receives new props → re-renders visualization
