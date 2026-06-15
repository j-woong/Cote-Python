def solution(n, words):
    word_counts = {i:0 for i in range(n)}
    used_words = set()
    
    prev_last_w = words[0][-1]
    used_words.add(words[0])
    word_counts[0] += 1
    
    for i in range(1,len(words)):
        num_circul = i % n
        word_counts[num_circul] += 1
          
        if words[i] in used_words or prev_last_w != words[i][0]:
            return [num_circul + 1, word_counts[num_circul]]
            
        used_words.add(words[i])
        prev_last_w = words[i][-1]
        
    return [0, 0]