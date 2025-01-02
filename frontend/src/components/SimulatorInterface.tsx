import { useEffect, useState } from 'react';
import { loadPyodide } from 'pyodide';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Loader2 } from 'lucide-react';

const SimulatorInterface = () => {
  const [pyodide, setPyodide] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function initPyodide() {
      try {
        const pyodideInstance = await loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.27.0/full",
        });
        
        // Import your simulator module
        await pyodideInstance.loadPackage(['micropip', './simulator/runner_sim-0.1.0-py3-none-any.whl']);
        await pyodideInstance.runPythonAsync(`
import micropip

await micropip.install('scipy==1.14.1', 'numpy==2.2.1')

from runner_sim import Runner

# Initialize a runner and store it in the global scope
runner = Runner(name="John", age=25)
globals()["runner"] = runner
        `);
        
        setPyodide(pyodideInstance);
        setLoading(false);
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError(String(err));
        }
        setLoading(false);
      }
    }

    initPyodide();
  }, []);

  const runSimulation = async () => {
    if (!pyodide) return;

    try {
      setLoading(true);
      const result = await pyodide.runPythonAsync(`
import random

from runner_sim import Activity, WorkoutTypes, TerrainTypes

# Retrieve the runner from the global scope
runner = globals()["runner"]
current_day = len(runner.daily_training_load)

# Generate a random activity
pace = random.uniform(6, 12)  # Pace in min/mile
distance = random.uniform(3, 20)   # Distance in miles
workout_type = random.choice(list(WorkoutTypes))
course_type = random.choice(list(TerrainTypes))
activity = Activity(pace=pace, distance=distance, workout_type=workout_type, course_type=course_type)

# Calculate the runner's new training load
runner.add_training_load(activity).sleep()

f"Day {current_day}: {runner.name}'s acute load: {runner.acute_training_load}"
      `);
      setResult(result);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError(String(err));
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="w-full max-w-2xl">
      <CardHeader>
        <CardTitle>Python Simulator</CardTitle>
      </CardHeader>
      <CardContent>
        {loading ? (
          <div className="flex items-center justify-center p-4">
            <Loader2 className="h-6 w-6 animate-spin" />
          </div>
        ) : error ? (
          <div className="text-red-500 p-4">
            Error: {error}
          </div>
        ) : (
          <div className="space-y-4">
            <Button onClick={runSimulation}>
              Run Simulation
            </Button>
            {result && (
              <pre className="bg-gray-100 p-4 rounded">
                {JSON.stringify(result, null, 2)}
              </pre>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default SimulatorInterface;