from collections import defaultdict

def solution(genres, plays):
    answer = []
    music_dict = defaultdict(list)
    # create hash
    for i, (genre, play) in enumerate(zip(genres, plays)):
        music_dict[genre].append((i, play))
    music_dict = sorted(music_dict.items(), key=lambda x: sum(play for i,play in x[1]), reverse=True)
    for k, v in music_dict:
        v.sort(key=lambda x:x[1], reverse=True)
    for k, v in music_dict:
        answer.extend([v[0] for v in v[:2]])
    return answer
