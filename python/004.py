class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_num = len(nums1)+len(nums2)
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        
        median_index = total_num/2 + 1
        # print("tots: ", total_num, "n1 = ", nums1_len, "n2 = ", nums2_len, "median = ", median_index)
        
        nums1_index = 1
        nums2_index = 1
        final_list = []
        
            
        for i in range(median_index):
            if nums1_index > nums1_len and nums2_index <= nums2_len:
                # print("Yo")
                final_list.append(nums2[nums2_index-1])
                nums2_index += 1
            elif nums1_index <= nums1_len and nums2_index > nums2_len:
                # print("Ho")
                final_list.append(nums1[nums1_index-1])
                nums1_index += 1
            else:
                if nums2[nums2_index-1] > nums1[nums1_index-1]:
                    # print("Fist:",nums2[nums2_index-1], nums1[nums1_index-1])
                    final_list.append(nums1[nums1_index-1])
                    nums1_index += 1
                else:
                    # print("Second:",nums2[nums2_index-1], nums1[nums1_index-1])
                    final_list.append(nums2[nums2_index-1])
                    nums2_index += 1
            # print final_list
        
        if total_num%2 == 0:
            return (final_list[-1] + final_list[-2]) * 1.0 / 2
        else:
            return final_list[-1]*1.0

                
            