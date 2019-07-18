// Fisher-Yates 洗牌算法可以把一个数组打散重新生成一个随机的数组。
// 
// 有 n 个数字，下标从 0 到 n-1。
// 算法描述：
// 1、从 n-1 开始(记为 lastIdx)，随机获取 0 到 n-1 中的数字 i；
// 2、i 和 lastIdx 互换位置；
// 3、lastIdx 减 1，继续从第 1 步开始，直到 lastIdx 到 0。


func shuffle(indexes []int) {
    for i:= len(indexes); i>0; i-- {
        lastIdx := i - 1
        idx := rand.Int(i)
        indexes[lastIdx], indexes[idx] = indexes[idx], indexes[lastIdx]
    }
}

