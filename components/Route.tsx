import { BrowserRouter as Router, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Route path="/industry/:id" component={Home} />
    </Router>
  );
}

export default App;