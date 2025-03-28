/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private double[] percThres;
    private double conf95 = 1.96;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        validate(n);
        validate(trials);
        percThres = new double[trials];
        for (int i = 0; i < trials; i++) {
            int randomRow = 0;
            int randomCol = 0;
            Percolation newPercolation = new Percolation(n);
            while (!newPercolation.percolates()) {
                randomRow = StdRandom.uniformInt(n);
                randomCol = StdRandom.uniformInt(n);
                newPercolation.open(randomRow + 1, randomCol + 1);
            }
            percThres[i] = (double) newPercolation.numberOfOpenSites() / (n * n);
        }
    }

    // validate that p is a valid index
    private void validate(int p) {
        if (p < 1) {
            throw new IllegalArgumentException(p + " is not greater than 0");
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(percThres);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(percThres);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - ((conf95 * stddev()) / Math.sqrt(percThres.length));
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + ((conf95 * stddev()) / Math.sqrt(percThres.length));
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats percolationStats = new PercolationStats(n, trials);
        StdOut.println(
                String.format("mean                    = %01.16f",
                              percolationStats.mean()));
        StdOut.println(
                String.format("stddev                  = %01.16f",
                              percolationStats.stddev()));
        StdOut.println(
                String.format("95%% confidence interval = [%01.16f, %01.16f]",
                              percolationStats.confidenceLo(), percolationStats.confidenceHi()));

    }
}
