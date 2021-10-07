class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var i = m-1
        var j = n-1

        if(m==0){
            nums2.forEachIndexed{ index, value ->
                nums1[index] = value
            }
            return
        }else if(n==0) return

        for(index in m+n-1 downTo 0){
            for(i in nums1){print(i)}
            println("before")
            println("index: $index, i:$i, j:$j")
            if(nums1[i] < nums2[j]){
                nums1[index] = nums2[j]
                nums2[j] = 0
                j -= 1
            }else{
                nums1[index] = nums1[i]
                nums1[i] = 0
                i -= 1
            }
            for(i in nums1){print(i)}
            if(j<0) break	
            if(i<0) {
                for(rest in 0..j){nums1[rest] = nums2[rest]}
                break
            }
        }
    }
}