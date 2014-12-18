package greetings;

import printing.*;

import java.io.File;
import java.io.IOException;
import java.util.HashSet;
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

        Set<Integer> mySet = new HashSet<Integer>();
        mySet.add(1);
        mySet.add(2);
        mySet.add(3);
        mySet.add(1);
        System.out.println(mySet.size());

        Set<String> anotherSet = new HashSet<String>();
        anotherSet.add("a");
        anotherSet.add("b");
        anotherSet.add("aaa");
        anotherSet.add("aa" + "a");
        anotherSet.add("ab");

        System.out.println(anotherSet.size());
        System.out.println(anotherSet.toString());
    }
}
