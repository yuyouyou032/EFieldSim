```
cd backend
pip install -r requirements.txt
uvicorn server:app --reload --port 8000
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
