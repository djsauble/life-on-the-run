import { useEffect, useState } from 'react';
import { loadPyodide } from 'pyodide';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Loader2 } from 'lucide-react';

const SimulatorInterface = () => {
  const [pyodide, setPyodide] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState<string | null>("Day 0: You are starting your fitness journey!");
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
from runner_sim import Singleton
sim = Singleton()
sim.initialize_runner()
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

  const doIntervals = async () => {
    await runSimulation('do_intervals');
  };

  const doTempoRun = async () => {
    await runSimulation('do_tempo_run');
  };

  const doRecoveryRun = async () => {
    await runSimulation('do_recovery_run');
  };

  const runSimulation = async (method: string) => {
    if (!pyodide) return;

    try {
      setLoading(true);
      const result = await pyodide.runPythonAsync(`
from runner_sim import Singleton
sim = Singleton()
sim.${method}()
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
        <CardTitle>Running Simulator</CardTitle>
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
            Improve your fitness without getting injured!<br/>
            <Button onClick={doIntervals}>
              Run intervals
            </Button>&nbsp;
            <Button onClick={doTempoRun}>
              Tempo run
            </Button>&nbsp;
            <Button onClick={doRecoveryRun}>
              Recovery run
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