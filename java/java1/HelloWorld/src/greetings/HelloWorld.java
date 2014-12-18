package greetings;

import printing.*;

import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/**
 * Created by rwehner on 12/16/14.
 */
public class HelloWorld {
    public static void main(String[] args)
    {
        Printer<BWCartridge> printer = new Printer<BWCartridge>(true, "My Printer", new BWCartridge());
        //printer.loadPaper(5);
        //printer.print(2);
        //printer.getPages();

        Queue<String> myQueue = new LinkedList<String>();

        myQueue.offer("a");
        myQueue.offer("b");
        myQueue.offer("c");

        while(myQueue.peek() != null) {
            System.out.println(myQueue.poll());
        }

    }
}
