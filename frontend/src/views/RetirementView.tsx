// import { useNavigate } from 'react-router-dom';

// function RetirementView() {
//   const navigate = useNavigate();

//   return (
//     <div className="flex flex-col items-center justify-center min-h-screen">
//       <h1 className="text-3xl font-bold mb-8">Retirement</h1>
//       <button
//         onClick={() => navigate('/')}
//         className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
//       >
//         Start New Game
//       </button>
//     </div>
//   );
// }

// export default RetirementView;

import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSimulator } from '../context/SimulatorContext';
import { RunnerProfile } from '../types/game';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Loader2 } from 'lucide-react';

function RetirementView() {
  const navigate = useNavigate();
  const { loading, error, initializeRunner } = useSimulator();
  const [profile, setProfile] = useState<RunnerProfile>({
    name: '',
    age: 25,
    weeklyMiles: 10,
    startingMoney: 5000,
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setProfile(prev => ({
      ...prev,
      [name]: name === 'name' ? value : Number(value),
    }));
  };

  const handleRestart = async (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Pass profile data to simulator
    navigate('/');
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <Loader2 className="h-6 w-6 animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-red-500">Error: {error}</div>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <Card className="w-full max-w-2xl">
        <CardHeader>
          <CardTitle>Career Summary</CardTitle>
        </CardHeader>
        <CardContent>
            <p className="py-4">
            You've decided to save what's left of your knees and retire at
            __.
            </p>
            
            <p className="py-4">
            Over the last __ years, you ran a total distance of __ miles,
            almost __ miles per week!
            </p>

            <p className="py-4">
            You ran __ races, with __ first place finishes, __ second place
            finishes, and __ third place finishes. You earned an
            astonishing $_____ in prize money and sponsorships.
            </p>

            <p className="py-4">
            The pinnacle of your career was running the __________ at
            age __, where you finished in ___ place and achieved a
            personal best time of __:__:__ at the _________ distance.
            </p>

            <p className="py-4">
            Not everyone can say that they literally chased their dreams,
            but you did.
            </p>

            <div className="flex justify-center">
              <Button type="submit" size="lg" onClick={() => navigate('/')}>
                Start New Game
              </Button>
            </div>
        </CardContent>
      </Card>
    </div>
  );
}

export default RetirementView;