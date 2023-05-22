import { createContext, useState } from "react";

const TodoContext = createContext()


export const TodoProvider = ({ children }) => {

    const [todos, setTodos] = useState("")
    const [isLoading, setisLoading] = useState(true)


    return (
        <TodoContext.Provider value={{
            'item': 5,
            todos,
            setTodos,
            isLoading,
            setisLoading

        }}>
            {children}
        </TodoContext.Provider>
    )
}


export default TodoContext