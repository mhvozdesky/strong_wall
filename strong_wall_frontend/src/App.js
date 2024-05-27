import './styles/App.css';
import LeftContent from './components/LeftContent'
import RightContent from './components/RightContent'

function App() {
  return (
    <div className="App">
      <div className='content'>
        <LeftContent />
        <RightContent />
      </div>
    </div>
  );
}

export default App;
