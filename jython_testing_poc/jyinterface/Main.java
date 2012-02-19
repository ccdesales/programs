package jyinterface;

import jyinterface.factory.EmployeeFactory;
import jyinterface.factory.JythonTesterFactory;
import jyinterface.interfaces.EmployeeType;
import jyinterface.interfaces.JythonTesterType;

public class Main {

    private static void print(EmployeeType employee) {
        System.out.println("Name: " + employee.getEmployeeFirst() + " "
                + employee.getEmployeeLast());
        System.out.println("Id: " + employee.getEmployeeId());
    }

    public static void main(String[] args) {
    	EmployeeFactory factory2 = new EmployeeFactory();
        print(factory2.create("Josh", "Juneau", "1"));
        print(factory2.create("Charlie", "Groves", "2"));
        
    	JythonTesterFactory factory = new JythonTesterFactory();
    	JythonTesterType tester = factory.create("cesar");
    	tester.runTest();
    }
}