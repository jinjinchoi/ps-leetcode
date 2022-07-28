def solution(nums):
    answer = 0

    pokemon_dict = {}
    for num in nums:
        pokemon_dict[num] = True

    return min(len(nums)//2, len(pokemon_dict.keys()))
