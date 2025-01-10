import { useNavigate } from 'react-router-dom';

function StartView() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-8">Training Simulator</h1>
      <button
        onClick={() => navigate('/observe')}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Start Game
      </button>
    </div>
  );
}

export default StartView;