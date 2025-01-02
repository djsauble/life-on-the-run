# Life on the Run

Manage the career of a cross-country runner

## Setup

Tested with Python 3.12.7

```
# Install dependencies for the simulator
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Complete 1000 activities at random until an injury occurs:

`python backend/src/simulate.py`

Manually interact with the simulator using a CLI:

`python backend/src/cli.py`