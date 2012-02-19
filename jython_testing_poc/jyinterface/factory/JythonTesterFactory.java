package jyinterface.factory;

import jyinterface.interfaces.JythonTesterType;

import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

public class JythonTesterFactory {
	private PyObject jyJythonTesterClass;
	
    public JythonTesterFactory() {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("from JythonTester import JythonTester");
        jyJythonTesterClass = interpreter.get("JythonTester");
    }

    public JythonTesterType create(String first) {
        PyObject testObj = jyJythonTesterClass.__call__(new PyString(first));
        return (JythonTesterType)testObj.__tojava__(JythonTesterType.class);
    }    
}