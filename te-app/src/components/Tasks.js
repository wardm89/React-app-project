import PropTypes from 'prop-types'
import Task from './Task'

const Tasks = ({tasks, onDelete, onToggle, on}) =>{
    return (
        <div>
            {tasks.map((task) => (
                <Task key={task.id} task={task} onDelete={onDelete} onToggle={onToggle}/>
            ))}

        </div>
    )
}



export default Tasks
