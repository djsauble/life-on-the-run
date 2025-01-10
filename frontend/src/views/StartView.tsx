import { useNavigate } from 'react-router-dom';
import { useSimulator } from '../context/SimulatorContext';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Loader2 } from 'lucide-react';

function StartView() {
  const navigate = useNavigate();
  const { loading, error, initializeRunner } = useSimulator();

  const handleStart = async () => {
    await initializeRunner();
    navigate('/observe');
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <Card className="w-full max-w-2xl">
        <CardHeader>
          <CardTitle>Training Simulator</CardTitle>
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
            <div className="flex flex-col items-center space-y-4">
              <p>Ready to start your training journey?</p>
              <Button onClick={handleStart}>
                Start Game
              </Button>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

export default StartView;