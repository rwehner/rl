package greetings;

import printing.*;
import sun.util.calendar.ZoneInfoFile;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class HelloWorld {
    public static void main(String[] args) {
        ContinuousPrinter cp = new ContinuousPrinter();
        //Thread thread = new Thread(cp);
        //thread.start();

        ExecutorService executor = Executors.newFixedThreadPool(100);
        executor.submit(cp);
        executor.submit(cp);
        executor.submit(cp);
        executor.submit(cp);
        executor.submit(cp);
        executor.submit(cp);
        executor.submit(cp);
        executor.shutdown();

        for(int i = 0; i < 100; i++)
            System.out.println("Main Thread " + i);

    }
}
