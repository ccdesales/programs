package jyinterface.factory;

import jyinterface.interfaces.EmployeeType;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

public class EmployeeFactory {
	private PyObject jyEmployeeClass;
	
    public EmployeeFactory() {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("from Employee import Employee");
        jyEmployeeClass = interpreter.get("Employee");
    }

    public EmployeeType create(String first, String last, String id) {
        PyObject employeeObj = jyEmployeeClass.__call__(new PyString(first),
                                                        new PyString(last),
                                                        new PyString(id));
        return (EmployeeType)employeeObj.__tojava__(EmployeeType.class);
    }    
}