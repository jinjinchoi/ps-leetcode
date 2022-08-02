
from collections import defaultdict

path_lengths = []

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # G 형성
    graph_hash = defaultdict(list)
    visited_hash = {word: False for word in [begin] + words}
    
    for word in words:
        if convertable(begin, word):
            graph_hash[begin].append(word)
    
    for word in words:
        for other_word in words:
            if convertable(word, other_word):
                graph_hash[word].append(other_word)
                
    # print(graph_hash)
    
    def dfs(begin, path_length, target):
        visited_hash[begin] = True
        
        if begin == target:
            # print("{} reached DONE!".format(target))
            path_lengths.append(path_length)
            # print(path_lengths)
            return
        
        for adjacent_node in graph_hash[begin]:
            if visited_hash[adjacent_node] == False:
                # print("{} => {}".format(begin, adjacent_node))
                dfs(adjacent_node, path_length+1, target)
                visited_hash[adjacent_node] = False    
                
    dfs(begin, 0, target)      
    
    
    return min(path_lengths)





def convertable(word1, word2):
    diff = 0
    for c1, c2 in zip(word1, word2):
        if c1!=c2:
            diff += 1
    return diff == 1

