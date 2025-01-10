import { useNavigate } from 'react-router-dom';

function DecideActView() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-8">Decide & Act</h1>
      <div className="space-x-4">
        <button
          onClick={() => navigate('/observe')}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Back to Observe
        </button>
        <button
          onClick={() => navigate('/retirement')}
          className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Retire
        </button>
      </div>
    </div>
  );
}

export default DecideActView;