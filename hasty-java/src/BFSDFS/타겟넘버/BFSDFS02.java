package BFSDFS.타겟넘버;

import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class BFSDFS02 {
    public int solution(int n, int[][] computers) {
        return getNetworkCount(getSquaredMatrix(computers));
    }

    public int[][] getSquaredMatrix(int[][] computers){
        int size = computers.length;
        int[][] squaredMatrix = new int[size][size];
        for(int rowIndex=0; rowIndex<size; rowIndex++){
            for(int colIndex=0; colIndex<size; colIndex++){
                int element = 0;
                for(int i=0; i<size; i++) element += computers[rowIndex][i]*computers[colIndex][i];
                squaredMatrix[rowIndex][colIndex] = element;
            }
        }
        return squaredMatrix;
    }

    public int getNetworkCount(int[][] squaredMatrix){
        Set<Integer> networkSet = new HashSet<>();
        int size = squaredMatrix.length;
        HashMap<Integer,Integer> networkMap = new HashMap<>();
        for(int rowIndex=0; rowIndex<size; rowIndex++){
            for(int colIndex=0; colIndex<size; colIndex++){
                if(networkMap.get(colIndex) == null && squaredMatrix[rowIndex][colIndex]>0) {
                    networkMap.put(colIndex, rowIndex);
                    networkSet.add(rowIndex);
                }
            }
        }
        return networkSet.size();
    }

    @Test
    public void checkAnswer() {
        int numCount1 = 3;
        int[][] computers1 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};

        int numCount2 = 3;
        int[][] computers2 = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};

        int numCount3 = 4;
        int[][] computers3 = {{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 0}, {1, 0, 0, 1}};

        int numCount4 = 5;
        int[][] computers4 = {{1, 0, 0, 1, 0}, {0, 1, 1, 0, 0}, {0, 1, 1, 0, 0}, {1, 0, 0, 1, 0}, {0, 0, 0, 0, 1}};

        int numCount5 = 5;
        int[][] computers5 = {{1, 0, 0, 1, 0, 0}, {0, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 0, 0}, {1, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0}, {0, 0, 0, 0, 0, 1}};


        assert 2 == solution(numCount1, computers1);
        assert 1 == solution(numCount2, computers2);
        assert 2 == solution(numCount3, computers3);
        assert 3 == solution(numCount4, computers4);
        assert 4 == solution(numCount5, computers5);
    }
}
