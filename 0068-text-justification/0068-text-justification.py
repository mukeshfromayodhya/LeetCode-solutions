class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#phase 1
        result = []
        current_line = []
        count = 0
        for word in words:
            if  len(current_line) == 0:
                current_line.append(word)
                count = len(word)
            elif count + 1 + len(word) <= maxWidth:
                current_line.append(word)
                count = count + len(word) + 1
            else:
                result.append(current_line)
                current_line = []
                count = 0
                current_line.append(word)
                count = len(word)
        result.append(current_line)
# phase 2
        final_result = []
        for index, i in enumerate(result):
            count = sum(len(word) for word in i)
            total_spaces = maxWidth - count
            gaps = len(i) - 1
            if gaps != 0:
                gap_min_space = total_spaces // gaps
                remainder = total_spaces % gaps
            if index == len(result) - 1:
                str_line = " ".join(i)
                current_length = len(str_line)
                remaining_spaces = maxWidth - current_length
                str_line = str_line + " " * remaining_spaces
                
            elif len(i) == 1:
                remaining_spaces = maxWidth - len(i[0])
                str_line = i[0] + " " * remaining_spaces
            else:
                str_line = ""
                for j in range(gaps):
                    str_line += i[j]
                    spaces = gap_min_space
                    if j < remainder:
                        spaces += 1
                    str_line += " " * spaces
                str_line += i[-1]
            final_result.append(str_line)
        return final_result