/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;

public class PercolationClient {
    public static void main(String[] args) {
        int n = 10;
        int randomRow = 0;
        int randomCol = 0;
        Percolation newPercolation = new Percolation(n);
        StdOut.println("isOpen: 9,1 -> " + newPercolation.isOpen(9, 1));
        StdOut.println("isFull: 9,1 -> " + newPercolation.isFull(9, 1));
        StdOut.println("opening 9,1");
        newPercolation.open(9, 1);
        StdOut.println("isOpen: 9,1 -> " + newPercolation.isOpen(9, 1));
        StdOut.println("is Full: 9,1 -> " + newPercolation.isFull(9, 1));
        StdOut.println("isOpen: 3,1 -> " + newPercolation.isOpen(3, 1));
        newPercolation.open(3, 1);
        StdOut.println("isOpen: 3,1 -> " + newPercolation.isOpen(3, 1));
        StdOut.println("isFull: 3,1 -> " + newPercolation.isFull(3, 1));
        StdOut.println("isOpen: 10,1 -> " + newPercolation.isOpen(10, 1));
        newPercolation.open(10, 1);
        StdOut.println("isOpen: 10,1 -> " + newPercolation.isOpen(10, 1));
        StdOut.println("isFull: 10,1 -> " + newPercolation.isFull(10, 1));
        newPercolation.open(1, 1);
        StdOut.println("isFull: 1,1 -> " + newPercolation.isFull(1, 1));
        newPercolation.open(4, 1);
        StdOut.println("isFull: 4,1 -> " + newPercolation.isFull(4, 1));
        newPercolation.open(7, 1);
        StdOut.println("isFull: 7,1 -> " + newPercolation.isFull(7, 1));
        newPercolation.open(5, 1);
        StdOut.println("isFull: 5,1 -> " + newPercolation.isFull(5, 1));
        newPercolation.open(6, 1);
        StdOut.println("isFull: 6,1 -> " + newPercolation.isFull(6, 1));
        newPercolation.open(2, 1);
        StdOut.println("isFull: 2,1 -> " + newPercolation.isFull(2, 1));
        newPercolation.open(8, 1);
        StdOut.println("isFull: 8,1 -> " + newPercolation.isFull(8, 1));
        StdOut.println("is Full: 9,1 -> " + newPercolation.isFull(9, 1));
        // while (!newPercolation.percolates()) {
        //     randomRow = StdRandom.uniformInt(n);
        //     randomCol = StdRandom.uniformInt(n);
        //     newPercolation.open(randomRow + 1, randomCol + 1);
        // }
        // StdOut.println(String.format("Percolates at %d.", newPercolation.numberOfOpenSites()));
    }
}
