/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */


import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String selectedWord = "";
        int i = 0;
        while (!StdIn.isEmpty()) {
            i = i + 1;
            double prob = 1.0 / i;
            boolean knuthProb = StdRandom.bernoulli(prob);
            String newWord = StdIn.readString();
            if (knuthProb) {
                selectedWord = newWord;
            }
        }
        StdOut.println(selectedWord);
    }
}
