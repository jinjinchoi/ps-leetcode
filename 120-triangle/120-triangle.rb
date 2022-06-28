# @param {Integer[][]} triangle
# @return {Integer}
def minimum_total(triangle)
    @height = triangle.size
    @result = Array.new(@height+1, 0)
    for row in (@height-1).downto(0)
        # puts "triangle[#{row}] #{triangle[row]}"
        triangle[row].each_with_index {|val, index| 
            @result[index] = val + (if @result[index] > @result[index+1] then @result[index+1] else @result[index] end)
            # puts "@result[#{index}]: #{@result[index]}"
        }
    end
    return @result[0]
end