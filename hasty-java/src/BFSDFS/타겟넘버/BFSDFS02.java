package BFSDFS.타겟넘버;

public class BFSDFS02 {
    int networkCount;
    public int solution(int n, int[][] computers) {
        networkCount = 0;
        int[] marked = new int[n];
        for(int row=0; row<n; row++){
            if(marked[row]==0) {
                networkCount += 1;
                DFS(row, computers, marked);
            }
        }
        return networkCount;
    }

    public void DFS(int row, int[][] computers, int[] marked){
        marked[row] = 1;
        for(int col=0; col<computers.length; col++){
            if(marked[col]==0 && computers[row][col]==1) DFS(col, computers, marked);
        }
    }
}

class TestBFSDFS02{
    @org.junit.jupiter.api.Test
    public void checkAnswer() {
        int numCount1 = 3;
        int[][] computers1 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};

        int numCount2 = 3;
        int[][] computers2 = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};

        int numCount3 = 4;
        int[][] computers3 = {{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 0}, {1, 0, 0, 1}};

        int numCount4 = 5;
        int[][] computers4 = {{1, 0, 0, 1, 0}, {0, 1, 1, 0, 0}, {0, 1, 1, 0, 0}, {1, 0, 0, 1, 0}, {0, 0, 0, 0, 1}};

        int numCount5 = 6;
        int[][] computers5 = {{1, 0, 0, 1, 0, 0}, {0, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 0, 0}, {1, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0}, {0, 0, 0, 0, 0, 1}};



        BFSDFS02 sol = new BFSDFS02();
        assert 2 == sol.solution(numCount1, computers1);
        assert 1 == sol.solution(numCount2, computers2);
        assert 2 == sol.solution(numCount3, computers3);
        assert 3 == sol.solution(numCount4, computers4);
        assert 4 == sol.solution(numCount5, computers5);
    }
}
