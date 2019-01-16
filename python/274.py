class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max_h = len(citations)
        histogram = [0]*(max_h+1)  

        for paper_citation in citations:
            if paper_citation > max_h:
                histogram[max_h] += 1
            else:
                histogram[paper_citation] += 1
        
        num_paper_above_hindex = 0
        
        for i in range(max_h,-1,-1):
            num_paper_above_hindex += histogram[i]
            if num_paper_above_hindex>=i:
                break
        
        return i
        