class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sortedCitations = sorted(citations, reverse=True)

        h_index = 0

        for i in range(len(sortedCitations)):
            h_index = max(h_index, min(sortedCitations[i], i + 1))
        return h_index