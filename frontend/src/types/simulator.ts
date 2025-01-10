export interface SimulatorState {
    pyodide: any | null;
    loading: boolean;
    result: string | null;
    error: string | null;
}