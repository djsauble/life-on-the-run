export interface Race {
    date: string;
    name: string;
    distance: string;
    successProbability: number;
    entryFee: number;
    prizeMoney: number;
}

export interface WorkoutPlan {
    duration: '30' | '60' | '90' | '120' | '240';
    type: 'Recovery' | 'Tempo' | 'Interval';
    course: 'Flat' | 'Rolling Hills' | 'Mountainous';
}