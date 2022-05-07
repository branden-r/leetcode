class Solution:
    def generate(self, row_count: int) -> list[list[int]]:
        # constraints tell us that the smallest pascal's triangle is one row of a single 1
        rows: list[list[int]] = [[1]]
        row_index: int  # need to iterate to generate the rest
        for row_index in range(1, row_count):
            rows.append(self.generate_row(rows[row_index - 1]))  # generate a new row based on the previous one
        return rows

    def generate_row(self, previous_row: list[int]) -> list[int]:
        # the start and end of a row will always be a 1 since they don't have two integers above them
        new_row: list[int] = [1, 1]
        index: int  # iterate through the previous row to build our new row
        # start iterating at index 1 and sum the integer at the current index and the one behind it
        # this creates integers for our new row in order
        # insert at index 1 so we insert between the two 1s we made for the beginning and end of the new row
        for index in range(1, len(previous_row)):
            new_row.insert(1, previous_row[index - 1] + previous_row[index])
        return new_row
