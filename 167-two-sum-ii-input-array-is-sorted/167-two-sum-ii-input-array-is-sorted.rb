# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    start_index = 0
    end_index = start_index + 1
    
    while (end_index < numbers.size) do
        # puts "numbers[#{start_index}] = #{numbers[start_index]}"
        # puts "numbers[#{end_index}] = #{numbers[end_index]}"
        if(numbers[start_index] + numbers[end_index] == target)
           return [start_index+1, end_index+1] 
        end
        if (end_index == numbers.size - 1 || numbers[start_index] + numbers[end_index] > target)
            current_start = numbers[start_index]
            until numbers[start_index] > current_start
                start_index += 1
            end
            end_index = start_index + 1
        else
            end_index += 1
        end
        
    end
    
    
end