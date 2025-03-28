/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */
public class PercolationTest {

    public static void main(String[] args) {
        // Create a 10x10 percolation grid
        Percolation percolation = new Percolation(10);

        // Test 1 - Simple Case: Vertical Path (Percolates, Full Sites)
        // Open a vertical path from (1, 1) to (10, 1)
        for (int row = 1; row <= 10; row++) {
            percolation.open(row, 1);
        }

        System.out.println("Test 1 - Simple Case: Vertical Path");
        System.out.println("Percolates: " + percolation.percolates()); // Expected: true
        for (int row = 1; row <= 10; row++) {
            System.out.println("Site (" + row + ", 1) is full: " + percolation.isFull(row,
                                                                                      1)); // Expected: true for all sites (1, 1) to (10, 1)
        }

        percolation = new Percolation(10);
        // Test 2 - Backwash Test 1: Connecting Top and Bottom, False Full Bottom Row
        // Open the path from (1, 1) to (9, 1), but leave (10, 1) closed
        for (int row = 1; row <= 9; row++) {
            percolation.open(row, 1);
        }

        System.out.println(
                "\nTest 2 - Backwash Test 1: Connecting Top and Bottom, False Full Bottom Row");
        System.out.println("Percolates: "
                                   + percolation.percolates()); // Expected: true (path from top to bottom exists)
        for (int row = 1; row <= 10; row++) {
            System.out.println("Site (" + row + ", 1) is full: " + percolation.isFull(row,
                                                                                      1)); // Expected: true for (1, 1) to (9, 1), false for (10, 1)
        }

        percolation = new Percolation(10);
        // Test 3 - Backwash Test 2: Multiple Paths (Multiple Columns)
        // Open vertical paths in columns 2, 3, and 4
        for (int col = 2; col <= 4; col++) {
            for (int row = 1; row <= 10; row++) {
                percolation.open(row, col);
            }
        }

        System.out.println("\nTest 3 - Backwash Test 2: Multiple Paths");
        System.out.println("Percolates: "
                                   + percolation.percolates()); // Expected: true (multiple paths from top to bottom)
        for (int col = 2; col <= 4; col++) {
            for (int row = 1; row <= 10; row++) {
                System.out.println(
                        "Site (" + row + ", " + col + ") is full: " + percolation.isFull(row,
                                                                                         col)); // Expected: true for all sites in columns 2, 3, and 4
            }
        }

        percolation = new Percolation(10);
        // Test 4 - Backwash Test 3: Non-continuous Path
        // Open disconnected sites along the diagonal (1, 1), (2, 2), ..., (6, 6)
        for (int i = 1; i <= 6; i++) {
            percolation.open(i, i);
        }

        System.out.println("\nTest 4 - Backwash Test 3: Non-continuous Path");
        System.out.println("Percolates: "
                                   + percolation.percolates()); // Expected: false (no continuous path from top to bottom)
        for (int row = 1; row <= 10; row++) {
            System.out.println("Site (" + row + ", 10) is full: " + percolation.isFull(row,
                                                                                       10)); // Expected: false for all sites in the 10th row
        }

        percolation = new Percolation(10);
        // Test 5 - Test for Backwash at the Bottom of the Grid
        // Open some disconnected sites but no full path from top to bottom
        percolation.open(1, 1);
        percolation.open(2, 2);
        percolation.open(3, 3);
        percolation.open(10, 10);

        System.out.println("\nTest 5 - Test for Backwash at the Bottom");
        System.out.println("Percolates: "
                                   + percolation.percolates()); // Expected: false (no continuous path from top to bottom)
        for (int col = 1; col <= 10; col++) {
            System.out.println("Site (" + col + ", 10) is full: " + percolation.isFull(col,
                                                                                       10)); // Expected: false for all sites in the bottom row
        }

        percolation = new Percolation(10);
        // Test 6 - Disconnected Row
        // Open two disconnected sites in the first row: (1, 1) and (1, 6)
        percolation.open(1, 1);
        percolation.open(1, 6);

        System.out.println("\nTest 6 - Disconnected Row");
        System.out.println("Percolates: "
                                   + percolation.percolates()); // Expected: false (no continuous path from top to bottom)
        for (int col = 1; col <= 10; col++) {
            System.out.println("Site (" + col + ", 10) is full: " + percolation.isFull(col,
                                                                                       10)); // Expected: false for all sites in the 10th row
        }
    }
}
