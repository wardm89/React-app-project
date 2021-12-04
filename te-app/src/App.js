import React from 'react'
import {useState} from 'react'
import Header from './components/Header'
import TheContainer from './components/Container'
import TheButton from './components/Button'
import Tasks from './components/Tasks'
import AddTask from './components/AddTask'

const App = () => {
    const [showAddTask, setShowAddTask] = useState(false)

    const [tasks, setTasks] = useState([
    {
        id: 1,
        text: 'Doctors Appointment',
        day: 'Feb 5th at 2:30pm',
        reminder: true,
    },
    {
        id: 2,
        text: '2nd Appointment',
        day: 'Feb 5th at 2:30pm',
        reminder: false,
    },
    {
        id: 3,
        text: '3rd Appointment',
        day: 'Feb 7th at 2:30pm',
        reminder: true,
    }
])

    //Delete Task
    const deleteTask = (id) => {
        setTasks(tasks.filter((task) => task.id !== id))
    }

    //Toggle Reminder
    const toggleReminder = (id) => {
        setTasks(
            tasks.map(task =>
            (task.id === id ? {...task, reminder: !task.reminder} : task)
        ))
    }
    //Add Task
    const addTask = (task) => {
        const id = Math.floor(Math.random() *10000) +1
        const newTask = {id, ...task}
        setTasks([...tasks, newTask])
    }

  return (
    <div className="container">
     <Header title={'Hello'} onAdd={() => setShowAddTask(!showAddTask)} showAdd={showAddTask}/>
        {showAddTask && <AddTask onAdd={addTask}/>}
        {tasks.length > 0 ? <Tasks tasks={tasks} onDelete={deleteTask} onToggle={toggleReminder}/> : 'No tasks'}
    </div>
  );
}

// class App extends React.Component{
//     render() {
//         return <Header/>
//     }
// }



export default App;
