




def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        index_1 = length // 2-1
        index_2 = length // 2 
        return (sorted_lst[index_1]) 