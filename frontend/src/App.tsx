import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import StartView from './views/StartView';
import ObserveOrientView from './views/ObserveOrientView';
import DecideActView from './views/DecideActView';
import RetirementView from './views/RetirementView';

function App() {
  return (
    <Router basename={import.meta.env.BASE_URL}>
      <div className="container mx-auto p-4">
        <Routes>
          <Route path="/" element={<StartView />} />
          <Route path="/observe" element={<ObserveOrientView />} />
          <Route path="/decide" element={<DecideActView />} />
          <Route path="/retirement" element={<RetirementView />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;