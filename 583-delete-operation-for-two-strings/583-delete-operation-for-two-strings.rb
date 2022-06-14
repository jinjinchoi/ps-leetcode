# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    row_num = word1.size
    col_num = word2.size
    dp_array = Array.new(row_num+1){Array.new(col_num+1, 0)} 
    for r in 0..row_num do
        dp_array[r][0] = r
    end
    for c in 0..col_num do
        dp_array[0][c] = c
    end
    for r in 1..row_num do
        for c in 1..col_num do
            if(word1[r-1] == word2[c-1])
                dp_array[r][c] = dp_array[r-1][c-1]
            else
                dp_array[r][c] = [dp_array[r][c-1], dp_array[r-1][c]].min + 1
            end
        end
    end
    return dp_array[row_num][col_num]
end