# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
    if(n==0)
        return nums1
    elsif (m==0)
        for i in 0..n-1 do
            nums1[i] = nums2[i]
        end
    else
        last_index = m+n-1
        index_1 = m-1
        index_2 = n-1
        
        while index_1 >= 0 && index_2 >= 0 do
           if  nums1[index_1] > nums2[index_2]
               nums1[last_index] = nums1[index_1]
               index_1 -= 1
           else
               nums1[last_index] = nums2[index_2]
               index_2 -= 1
           end
            last_index -= 1
        end
        
        if (index_2 >= 0) 
            for i in 0..index_2 do
                nums1[i] = nums2[i]
            end
        end
    end
    return nums1
end