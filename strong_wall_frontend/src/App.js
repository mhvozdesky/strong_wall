import './styles/App.css';
import LeftContent from './components/LeftContent'
import RigntContent from './components/RigntContent'

function App() {
  return (
    <div className="App">
      <div className='content'>
        <LeftContent />
        <RigntContent />
      </div>
    </div>
  );
}

export default App;
