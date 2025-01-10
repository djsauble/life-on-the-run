import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSimulator } from '../context/SimulatorContext';
import { Race, WorkoutPlan } from '../types/training';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
import { Label } from '@/components/ui/label';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';

function DecideActView() {
  const navigate = useNavigate();
  const { runSimulation } = useSimulator();

  // Mock data - replace with simulator data later
  const [races] = useState<Race[]>([
    {
      date: '2024-02-01',
      name: 'Winter 5K Challenge',
      distance: '5K',
      successProbability: 0.75,
      entryFee: 30,
      prizeMoney: 500
    },
    {
      date: '2024-03-15',
      name: 'Spring Half Marathon',
      distance: 'Half Marathon',
      successProbability: 0.45,
      entryFee: 80,
      prizeMoney: 2000
    },
    {
      date: '2024-04-30',
      name: 'City Marathon',
      distance: 'Marathon',
      successProbability: 0.25,
      entryFee: 150,
      prizeMoney: 5000
    }
  ]);

  const [workout, setWorkout] = useState<WorkoutPlan>({
    duration: '60',
    type: 'Recovery',
    course: 'Flat'
  });

  const handleSignUp = (race: Race) => {
    // TODO: Implement race registration
    console.log('Signing up for race:', race);
  };

  const handleWorkoutChange = (field: keyof WorkoutPlan, value: WorkoutPlan[keyof WorkoutPlan]) => {
    setWorkout(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const handlePlanWorkout = async () => {
    // TODO: Connect to simulator
    console.log('Planning workout:', workout);
  };

  return (
    <div className="container mx-auto p-4 space-y-6">
      <Card>
        <CardHeader>
          <CardTitle>Sign up for a race</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Date</TableHead>
                <TableHead>Race</TableHead>
                <TableHead>Distance</TableHead>
                <TableHead>Success</TableHead>
                <TableHead>Entry Fee</TableHead>
                <TableHead>Prize</TableHead>
                <TableHead></TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {races.map((race) => (
                <TableRow key={`${race.date}-${race.name}`}>
                  <TableCell>{race.date}</TableCell>
                  <TableCell>{race.name}</TableCell>
                  <TableCell>{race.distance}</TableCell>
                  <TableCell>{(race.successProbability * 100).toFixed(0)}%</TableCell>
                  <TableCell>${race.entryFee}</TableCell>
                  <TableCell>${race.prizeMoney}</TableCell>
                  <TableCell>
                    <Button
                      variant="secondary"
                      size="sm"
                      onClick={() => handleSignUp(race)}
                    >
                      Sign Up
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Plan your workouts for the week</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-6">
            <div className="space-y-2">
              <Label>Duration</Label>
              <RadioGroup
                value={workout.duration}
                onValueChange={(value) => handleWorkoutChange('duration', value as WorkoutPlan['duration'])}
                className="flex flex-wrap gap-4"
              >
                {['30', '60', '90', '120', '240'].map((duration) => (
                  <div key={duration} className="flex items-center space-x-2">
                    <RadioGroupItem value={duration} id={`duration-${duration}`} />
                    <Label htmlFor={`duration-${duration}`}>{duration} min</Label>
                  </div>
                ))}
              </RadioGroup>
            </div>

            <div className="space-y-2">
              <Label>Workout type</Label>
              <RadioGroup
                value={workout.type}
                onValueChange={(value) => handleWorkoutChange('type', value as WorkoutPlan['type'])}
                className="flex flex-wrap gap-4"
              >
                {['Recovery', 'Tempo', 'Interval'].map((type) => (
                  <div key={type} className="flex items-center space-x-2">
                    <RadioGroupItem value={type} id={`type-${type}`} />
                    <Label htmlFor={`type-${type}`}>{type}</Label>
                  </div>
                ))}
              </RadioGroup>
            </div>

            <div className="space-y-2">
              <Label>Course type</Label>
              <RadioGroup
                value={workout.course}
                onValueChange={(value) => handleWorkoutChange('course', value as WorkoutPlan['course'])}
                className="flex flex-wrap gap-4"
              >
                {['Flat', 'Rolling Hills', 'Mountainous'].map((course) => (
                  <div key={course} className="flex items-center space-x-2">
                    <RadioGroupItem value={course} id={`course-${course}`} />
                    <Label htmlFor={`course-${course}`}>{course}</Label>
                  </div>
                ))}
              </RadioGroup>
            </div>
          </div>

          <div className="mt-6 flex justify-end space-x-4">
            <Button variant="secondary" onClick={() => navigate('/observe')}>
              Back to Overview
            </Button>
            <Button onClick={handlePlanWorkout}>
              Plan Workout
            </Button>
            <Button variant="destructive" onClick={() => navigate('/retirement')}>
              Retire
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

export default DecideActView;