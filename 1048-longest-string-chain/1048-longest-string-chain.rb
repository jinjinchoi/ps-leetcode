# @param {String[]} words
# @return {Integer}
def longest_str_chain(words)
    words_size = words.size
    sorted_words =  words.sort_by {|x| x.length}
    result_hash = sorted_words.to_h { |x| [x, 1] }
    
    for i in 0..words_size-1 do
       word =  sorted_words[i]
        word.each_char.with_index do |char, index|
           # puts "#{word}'s substr, index #{index}: #{word.slice(0, index)+word.slice(index+1, word.length)}"
           sliced_word = word.slice(0, index)+word.slice(index+1, word.length)
          if words.include?(sliced_word)
              # puts "..is inside words! --- result_hash[sliced_word] #{result_hash[sliced_word]}, result_hash[word] #{result_hash[word]}"
              result_hash[word] = [result_hash[sliced_word]+1, result_hash[word]].max
              # puts "updated: "
              # break
          end
        end 
    end
    return result_hash.values.max
end