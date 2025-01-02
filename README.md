# Life on the Run

Manage the career of a cross-country runner

## Setup

Tested with Python 3.12.7 and Node 22.12.10

```
# Switch to the backend directory
cd backend/

# Install dependencies for the simulator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Build the simulator
python -m build --wheel
cp dist/runner_sim*.whl ../frontend/public/simulator/

# Switch back to the root of the project directory
cd ..
```

## Run

Complete 1000 activities at random until an injury occurs:

```
python backend/src/simulate.py
```

Manually interact with the simulator using a CLI:

```
python backend/src/cli.py
```

Run the simulator web interface:

```
cd frontend/
npm install
npm run dev
```

Open http://localhost:5173 in your browser