package greetings;

import printing.*;

import java.io.File;
import java.io.IOException;

/**
 * Created by rwehner on 12/16/14.
 */
public class HelloWorld {
    public static void main(String[] args)
    {
        Printer<BWCartridge> printer = new Printer<BWCartridge>(true, "My Printer", new BWCartridge());

        try {

            printer.print(-1);
        }
        catch (IllegalArgumentException exception) {
            System.out.println(exception.getMessage());
            return;
        }
        finally {
            printer.TurnOff();
        }
    }
}
