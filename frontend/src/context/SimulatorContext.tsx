import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { loadPyodide } from 'pyodide';
import { SimulatorState } from '../types/simulator';

interface SimulatorContextType extends SimulatorState {
  initializeRunner: () => Promise<void>;
  runSimulation: (method: string) => Promise<void>;
}

const SimulatorContext = createContext<SimulatorContextType | undefined>(undefined);

export function SimulatorProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<SimulatorState>({
    pyodide: null,
    loading: true,
    result: "Day 0: You are starting your fitness journey!",
    error: null,
  });

  useEffect(() => {
    async function initPyodide() {
      try {
        const pyodideInstance = await loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.27.0/full",
        });
        
        await pyodideInstance.loadPackage(['./simulator/runner_sim-0.1.0-py3-none-any.whl']);
        
        setState(prev => ({
          ...prev,
          pyodide: pyodideInstance,
          loading: false,
        }));
      } catch (err) {
        setState(prev => ({
          ...prev,
          error: err instanceof Error ? err.message : String(err),
          loading: false,
        }));
      }
    }

    initPyodide();
  }, []);

  const initializeRunner = async () => {
    if (!state.pyodide) return;

    try {
      setState(prev => ({ ...prev, loading: true }));
      await state.pyodide.runPythonAsync(`
from runner_sim import Singleton
sim = Singleton()
sim.initialize_runner()
      `);
      setState(prev => ({
        ...prev,
        loading: false,
        result: "Day 0: You are starting your fitness journey!",
        error: null,
      }));
    } catch (err) {
      setState(prev => ({
        ...prev,
        error: err instanceof Error ? err.message : String(err),
        loading: false,
      }));
    }
  };

  const runSimulation = async (method: string) => {
    if (!state.pyodide) return;

    try {
      setState(prev => ({ ...prev, loading: true }));
      const result = await state.pyodide.runPythonAsync(`
from runner_sim import Singleton
sim = Singleton()
sim.${method}()
      `);
      setState(prev => ({
        ...prev,
        loading: false,
        result,
        error: null,
      }));
    } catch (err) {
      setState(prev => ({
        ...prev,
        error: err instanceof Error ? err.message : String(err),
        loading: false,
      }));
    }
  };

  return (
    <SimulatorContext.Provider 
      value={{
        ...state,
        initializeRunner,
        runSimulation,
      }}
    >
      {children}
    </SimulatorContext.Provider>
  );
}

export function useSimulator() {
  const context = useContext(SimulatorContext);
  if (context === undefined) {
    throw new Error('useSimulator must be used within a SimulatorProvider');
  }
  return context;
}