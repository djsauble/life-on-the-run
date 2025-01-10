import { useNavigate } from 'react-router-dom';

function ObserveOrientView() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-8">Observe & Orient</h1>
      <button
        onClick={() => navigate('/decide')}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Continue to Decisions
      </button>
    </div>
  );
}

export default ObserveOrientView;