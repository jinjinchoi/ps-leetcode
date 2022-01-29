class MinStack() {
    private var topNode: StackNode? = null

    fun push(`val`: Int) {
        topNode?.let{
            val minValue = Math.min(topNode!!.`min`, `val`)
            var newNode = StackNode(`val`, minValue)
            newNode.bottom = topNode
            topNode = newNode
        } ?: run{
            var newNode = StackNode(`val`, `val`)
            topNode = newNode
        }
    }

    fun pop() {
        topNode = topNode!!.bottom
    }

    fun top(): Int {
        return topNode!!.`val`
    }

    fun getMin(): Int {
        return topNode!!.`min`
    }
}


class StackNode(var `val`: Int, var `min`: Int){
    var bottom: StackNode? = null
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = MinStack()
 * obj.push(`val`)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */