# @param {String} s
# @return {String}
def longest_palindrome(s)
    start_index = 0
    end_index = 0
    max_length = 0
    # odd-length palindrome
    for i in 0..s.size-1 do
        j = 1
        # puts "i: #{i} start, (i-j): #{i-j}, (i+j): #{i+j}"
        while ((i-j>=0) && (i+j<s.size))  do
          if(s[i-j] == s[i+j])
              # puts "i: #{i}, j: #{j}, s[#{i-j}] = s[#{i+j}]"
              if max_length < 1+2*j
                 max_length = 1+2*j
                 start_index = i-j
                 end_index = i+j
                 # puts "current max_length #{max_length} s[#{start_index}..#{end_index}]: #{s[start_index..end_index]}"
              end
              j+= 1
          else 
              break
          end
           
       end
    end
    
    # even-length palindrome
    for i in 0..s.size-1 do
        # puts "s[i]: #{s[i]}, s[i+1]: #{s[i+1]}"
        j = 0
         while ((i-j>=0) && (i+j+1<s.size))  do
          if(s[i-j] == s[i+j+1])
              # puts "i: #{i}, j: #{j}, s[#{i-j}] = s[#{i+j+1}]"
              if max_length < 2+2*j
                 max_length = 2+2*j
                 start_index = i-j
                 end_index = i+j+1
                 # puts "current max_length #{max_length} s[#{start_index}..#{end_index}]: #{s[start_index..end_index]}"
              end
              j+= 1
          else 
              break
          end
         end
           
    end
    return s[start_index..end_index]
    
end