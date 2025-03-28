/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private boolean[] opened;
    private WeightedQuickUnionUF perWQUUF;
    private WeightedQuickUnionUF perWQUUF4Full;
    private int openCount;
    private int dimension;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException(n + " is not between greater than 0");
        }
        dimension = n;
        perWQUUF = new WeightedQuickUnionUF(n * n + 2);
        perWQUUF4Full = new WeightedQuickUnionUF(n * n + 1);
        opened = new boolean[n * n + 2];
        for (int i = 0; i < n * n + 2; i++) {
            opened[i] = false;
        }
        opened[(dimension * dimension)] = true;
        opened[(dimension * dimension) + 1] = true;
        openCount = 0;
    }

    private int twoDToOneD(int row, int col) {
        validate(row);
        validate(col);
        row--;
        col--;
        // StdOut.println(
        //         String.format("index %d", (row * dimension) + col));
        return (row * dimension) + col;
    }

    // validate that p is a valid index
    private void validate(int p) {
        if (p < 1 || p > dimension) {
            throw new IllegalArgumentException("index " + p + " is not between 1 and " + dimension);
        }
    }

    // opens the site (row, col) if it is not opened already
    public void open(int row, int col) {
        // StdOut.println(String.format("open -> row: %d, col: %d", row, col));
        validate(row);
        validate(col);
        int oneDId = twoDToOneD(row, col);
        // StdOut.println(String.format("open -> oneDId: %d", oneDId));
        boolean hasUp = (row != 1);
        boolean hasLeft = (col != 1);
        boolean hasDown = (row != dimension);
        boolean hadRight = (col != dimension);
        // StdOut.println(String.format("hasUp: %b | hasLeft: %b | hasDown: %b | hadRight: %b ", hasUp,
        //                              hasLeft, hasDown, hadRight));
        // StdOut.println(String.format("open -> isOpen(%d, %d): %b", row, col, isOpen(row, col)));
        if (!isOpen(row, col)) {
            // StdOut.println(String.format("open -> %d, %d not opened", row, col));
            opened[oneDId] = true;
            openCount++;
            // StdOut.println(String.format("open -> %d, %d not hasUp: %b", row, col, hasUp));
            if (!hasUp) {
                // StdOut.println(String.format("open -> %d, %d not hasUp: %b", row, col, hasUp));
                perWQUUF.union(oneDId, dimension * dimension);
                perWQUUF4Full.union(oneDId, dimension * dimension);
            }
            // StdOut.println(String.format("open -> %d, %d not hasDown: %b", row, col, hasDown));
            if (!hasDown) {
                // StdOut.println(String.format("open -> %d, %d not hasDown: %b", row, col, hasDown));
                perWQUUF.union(oneDId, (dimension * dimension) + 1);
            }
            // StdOut.println(
            //         String.format("open -> %d, %d hasUp: %b isOpen(%d, %d): %b", row, col, hasUp,
            //                       row - 1, col, isOpen(row - 1, col)));
            if (hasUp && isOpen(row - 1, col)) {
                // StdOut.println(
                //         String.format("open -> %d, %d hasUp: %b isOpen(%d, %d): %b", row, col,
                //                       hasUp, row - 1, col, isOpen(row - 1, col)));
                perWQUUF.union(oneDId, twoDToOneD(row - 1, col));
                perWQUUF4Full.union(oneDId, twoDToOneD(row - 1, col));
            }
            // StdOut.println(String.format("open -> %d, %d hasLeft: %b isOpen(%d, %d): %b", row, col,
            //                              hasLeft, row, col - 1, isOpen(row, col - 1)));
            if (hasLeft && isOpen(row, col - 1)) {
                // StdOut.println(
                //         String.format("open -> %d, %d hasLeft: %b isOpen(%d, %d): %b", row, col,
                //                       hasLeft, row, col - 1, isOpen(row, col - 1)));
                perWQUUF.union(oneDId, twoDToOneD(row, col - 1));
                perWQUUF4Full.union(oneDId, twoDToOneD(row, col - 1));
            }
            // StdOut.println(String.format("open -> %d, %d hasDown: %b isOpen(%d, %d): %b", row, col,
            //                              hasDown, row + 1, col, isOpen(row + 1, col)));
            if (hasDown && isOpen(row + 1, col)) {
                // StdOut.println(
                //         String.format("open -> %d, %d hasDown: %b isOpen(%d, %d): %b", row, col,
                //                       hasDown, row + 1, col, isOpen(row + 1, col)));
                perWQUUF.union(oneDId, twoDToOneD(row + 1, col));
                perWQUUF4Full.union(oneDId, twoDToOneD(row + 1, col));
            }
            // StdOut.println(String.format("open -> %d, %d hadRight: %b isOpen(%d, %d): %b", row, col,
            //                              hadRight, row, col + 1, isOpen(row, col + 1)));
            if (hadRight && isOpen(row, col + 1)) {
                // StdOut.println(
                //         String.format("open -> %d, %d hadRight: %b isOpen(%d, %d): %b", row, col,
                //                       hadRight, row, col + 1, isOpen(row, col + 1)));
                perWQUUF.union(oneDId, twoDToOneD(row, col + 1));
                perWQUUF4Full.union(oneDId, twoDToOneD(row, col + 1));
            }
            // StdOut.println(String.format("open -> %d, %d opened", row, col));
        }
    }

    // is the site (row, col) opened?
    public boolean isOpen(int row, int col) {
        // StdOut.println(String.format("isOpen -> row: %d, col: %d", row, col));
        validate(row);
        validate(col);
        int oneDId = twoDToOneD(row, col);
        return opened[oneDId];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        // StdOut.println(String.format("isFull -> row: %d, col: %d", row, col));
        validate(row);
        validate(col);
        int oneDId = twoDToOneD(row, col);
        return perWQUUF4Full.find(dimension * dimension) == perWQUUF4Full.find(oneDId);
    }

    // returns the number of opened sites
    public int numberOfOpenSites() {
        return openCount;
    }

    // does the system percolate?
    public boolean percolates() {
        // boolean percolates = false;
        // for (int i = dimension * (dimension - 1); i < dimension * dimension; i++) {
        //     // if (perWQUUF.find(dimension * dimension) == perWQUUF.find(i)) {
        //     if (perWQUUF.connected(dimension * dimension, i)) {
        //         percolates = true;
        //         break;
        //     }
        // }
        return perWQUUF.find(dimension * dimension) == perWQUUF.find((dimension * dimension) + 1);
    }

    public static void main(String[] args) {
        int n = StdIn.readInt();
        int randomRow;
        int randomCol;
        Percolation newPercolation = new Percolation(n);
        while (!newPercolation.percolates()) {
            randomRow = StdRandom.uniformInt(n);
            randomCol = StdRandom.uniformInt(n);
            newPercolation.open(randomRow + 1, randomCol + 1);
        }
        StdOut.println(
                String.format("percolation threshold %,.4f",
                              (double) newPercolation.numberOfOpenSites() / (n * n)));
    }
}
