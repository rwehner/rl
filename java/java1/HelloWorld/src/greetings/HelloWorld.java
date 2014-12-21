package greetings;

import printing.*;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class HelloWorld {
    public static void main(String[] args) {
        ContinuousPrinter cp = new ContinuousPrinter();
        cp.start();

        for(int i = 0; i < 100; i++)
            System.out.println("Main Thread " + i);

    }
}
