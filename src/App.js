import './App.css';
import userIcon from './images/whiteUserIcon.png';
import Logo from './images/tradersStatsLogo.png';

function App() {
  return (
    <div className="container-1">
    <div>
     <img src={Logo} className="image-2"/>
    </div>
    <div className="title-1">
       <h7>
         User Analysis
       </h7>
    </div>
    <div>
     <img src={userIcon} className="image-1"/>
    </div>
   </div>
  );
}

export default App;
