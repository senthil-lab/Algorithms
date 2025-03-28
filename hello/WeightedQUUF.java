/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

public class WeightedQUUF {

    private int[] id;

    public WeightedQUUF(int n) {
        id = new int[n];
        sz = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int rootp = root(p);
        int rootq = root(q);
        if (rootp == rootq) return;
        if (sz[rootp] < sz[rootp]) {
            id[rootp] = rootq;
            sz[rootq] = sz[rootq] + sz[rootp];
        }
        else {
            id[rootq] = rootp;
            sz[rootp] = sz[rootp] + sz[rootq];
        }
    }
}
