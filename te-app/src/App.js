import React from 'react'
import Header from './components/Header'
import TheContainer from './components/Container'
import TheButton from './components/Button'

const App = () => {
  return (
    <div className="App">
     <Header title={'Hello'}/>
     <TheContainer />
     <TheButton />
    </div>
  );
}

// class App extends React.Component{
//     render() {
//         return <Header/>
//     }
// }



export default App;
