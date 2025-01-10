import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSimulator } from '../context/SimulatorContext';
import { MonthlyExpense } from '../types/expenses';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Edit } from 'lucide-react';

function ObserveOrientView() {
  const navigate = useNavigate();
  const { result } = useSimulator();
  
  // Mock data - replace with actual simulator data later
  const [stats] = useState({
    cash: 5000,
    burnRate: 1500,
    daysRemaining: 100,
    nextEventDays: 30,
    fitness: 70,
    energy: 85,
    health: 95
  });

  const [expenses] = useState<MonthlyExpense[]>([
    { name: 'Shoes', amount: 200, period: 'monthly' },
    { name: 'Food', amount: 300, period: 'monthly' },
    { name: 'Rent', amount: 1000, period: 'monthly' },
  ]);

  const handleEdit = (expenseType: string) => {
    // TODO: Implement expense editing
    console.log(`Editing ${expenseType}`);
  };

  return (
    <div className="container mx-auto p-4">
      <Card className="mb-6">
        <CardHeader>
          <CardTitle>Status Overview</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-6">
            {/* Financial Status */}
            <div className="space-y-2">
              <p>You have ${stats.cash.toLocaleString()} on hand</p>
              <p className="text-muted-foreground">
                (this will last {stats.daysRemaining} days)
              </p>
              <p>Your next event is in {stats.nextEventDays} days.</p>
            </div>

            {/* Metrics */}
            <div className="grid gap-4">
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span>Fitness</span>
                  <span>{stats.fitness}%</span>
                </div>
                <Progress value={stats.fitness} />
              </div>
              
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span>Energy</span>
                  <span>{stats.energy}%</span>
                </div>
                <Progress value={stats.energy} />
              </div>
              
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span>Health</span>
                  <span>{stats.health}%</span>
                </div>
                <Progress value={stats.health} />
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Monthly Expenses</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {expenses.map((expense) => (
              <div key={expense.name} className="flex items-center justify-between border-b pb-2">
                <span>{expense.name}</span>
                <div className="flex items-center gap-4">
                  <span>${expense.amount} / month</span>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => handleEdit(expense.name)}
                  >
                    <Edit className="h-4 w-4" />
                    <span className="sr-only">Edit {expense.name}</span>
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      <div className="mt-6 flex justify-end">
        <Button onClick={() => navigate('/decide')}>
          Continue to Actions
        </Button>
      </div>

      {result && (
        <Card className="mt-6">
          <CardContent className="pt-6">
            <pre className="whitespace-pre-wrap">{result}</pre>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

export default ObserveOrientView;