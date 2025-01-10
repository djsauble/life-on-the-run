import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSimulator } from '../context/SimulatorContext';
import { RunnerProfile } from '../types/game';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Loader2 } from 'lucide-react';

function StartView() {
  const navigate = useNavigate();
  const { loading, error, initializeRunner } = useSimulator();
  const [profile, setProfile] = useState<RunnerProfile>({
    name: 'Daniel',
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

  const handleStart = async (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Pass profile data to simulator
    await initializeRunner();
    navigate('/observe');
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
          <CardTitle>Begin Your Running Career</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleStart} className="space-y-6">
            <div className="space-y-4">
              <div className="grid gap-2">
                <Label htmlFor="name">Your name is</Label>
                <Input
                  id="name"
                  name="name"
                  value={profile.name}
                  onChange={handleChange}
                  required
                  className="w-full"
                />
              </div>

              <div className="grid gap-2">
                <Label htmlFor="age">you're</Label>
                <div className="flex items-center gap-2">
                  <Input
                    id="age"
                    name="age"
                    type="number"
                    min="18"
                    max="65"
                    value={profile.age}
                    onChange={handleChange}
                    required
                    className="w-24"
                  />
                  <span>years old</span>
                </div>
              </div>

              <div className="grid gap-2">
                <Label htmlFor="weeklyMiles">and you run approximately</Label>
                <div className="flex items-center gap-2">
                  <Input
                    id="weeklyMiles"
                    name="weeklyMiles"
                    type="number"
                    min="0"
                    max="100"
                    value={profile.weeklyMiles}
                    onChange={handleChange}
                    required
                    className="w-24"
                  />
                  <span>miles per week.</span>
                </div>
              </div>

              <p className="text-center py-4">
                Against the advice of everyone you know, you've decided to
                become a professional long-distance runner. You quit your
                job this morning and signed up for your first 5K event.
              </p>

              <div className="grid gap-2">
                <Label htmlFor="startingMoney">You have a pair of running shoes and</Label>
                <div className="flex items-center gap-2">
                  <span>$</span>
                  <Input
                    id="startingMoney"
                    name="startingMoney"
                    type="number"
                    min="0"
                    max="100000"
                    step="100"
                    value={profile.startingMoney}
                    onChange={handleChange}
                    required
                    className="w-32"
                  />
                  <span>to your name.</span>
                </div>
              </div>
            </div>

            <div className="flex justify-center">
              <Button type="submit" size="lg">
                Start Your Journey
              </Button>
            </div>

            <p className="text-center text-sm text-muted-foreground">
              Good luck!
            </p>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}

export default StartView;