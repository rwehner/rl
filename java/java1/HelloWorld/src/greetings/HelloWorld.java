package greetings;

import printing.*;

import java.io.File;
import java.io.IOException;
import java.util.*;

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

        Map<String, List<Integer>> testScores = new HashMap<String, List<Integer>>();

        List<Integer> joesTestScores = new ArrayList<Integer>();
        joesTestScores.add(85);
        joesTestScores.add(97);
        joesTestScores.add(64);
        testScores.put("Joe", joesTestScores);

        List<Integer> amyTestScores = new ArrayList<Integer>();
        amyTestScores.add(99);
        amyTestScores.add(78);
        amyTestScores.add(100);
        amyTestScores.add(100);
        amyTestScores.add(100);
        amyTestScores.add(100);
        testScores.put("Amy", amyTestScores);

        List<Integer> fredTestScores = new ArrayList<Integer>();
        fredTestScores.add(100);
        fredTestScores.add(80);
        testScores.put("Fred", fredTestScores);

        printScores("Joe", testScores);
        printScores("Amy", testScores);
        printScores("Fred", testScores);
    }

    public static void printScores(String studentName, Map<String, List<Integer>> scoresMap) {
        List<Integer> studentScores = scoresMap.get(studentName);
        System.out.println(studentName + ":");
        for( int score : studentScores) {
            System.out.println("\t" + score);
        }
    }
}
