# @param {Integer} n
# @return {Integer}
require 'set'


def total_n_queens(n)
    @distinct_cols = Set.new
    @pos_diags = Set.new
    @neg_diags = Set.new

    @count = 0
    placeOnRow(0, n)
    return @count
end


def placeOnRow(row, n)
    if(row == n)
       @count += 1
       return
    end

    for col in 0..n-1 do
        if(@distinct_cols.include?(col) || @pos_diags.include?(row+col) || @neg_diags.include?(row-col)) 
            next
        end
        
        @distinct_cols.add(col)
        @pos_diags.add(col+row)
        @neg_diags.add(row-col)
        
        placeOnRow(row+1, n)
        
        @distinct_cols.delete(col)
        @pos_diags.delete(col+row)
        @neg_diags.delete(row-col)   
    end
end