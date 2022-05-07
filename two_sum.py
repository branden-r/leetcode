class Solution:
    def twoSum(self, integers: list[int], target: int) -> list[int]:
        solution_indexes: list[int] = []
        # as we iterate, map integers to their index
        # this way, we don't have to search for an integer we've already seen - we already know where it is via the map
        index_map: dict[int, int] = {}
        index: int
        integer: int
        for index, integer in enumerate(integers):  # use enumerate to access the indices
            # partner is the number we need to add to the current integer to get the target
            partner: int = target - integer
            if partner in index_map:  # if we've seen this number already, we're done
                solution_indexes.extend((index, index_map[partner]))
                break  # stop searching because due to constraints (exactly one solution)
            index_map[integer] = index  # we didn't find a solution, so update the map and move to the next integer
        return solution_indexes
