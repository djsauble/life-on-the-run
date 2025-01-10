import { useNavigate } from 'react-router-dom';

function RetirementView() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-8">Retirement</h1>
      <button
        onClick={() => navigate('/')}
        className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
      >
        Start New Game
      </button>
    </div>
  );
}

export default RetirementView;