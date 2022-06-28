/* The isBadVersion API is defined in the parent class VersionControl.
      fun isBadVersion(version: Int) : Boolean {} */

class Solution: VersionControl() {
    var startIndex = 1
    var endIndex = 1
    var nextIndex = 1
    
    override fun firstBadVersion(n: Int) : Int {
        endIndex = n
        while(startIndex < endIndex){
            nextIndex = startIndex + (endIndex - startIndex)/2
            if(isBadVersion(nextIndex)) endIndex = nextIndex
            else startIndex = nextIndex + 1
        }
        return endIndex
	}
}