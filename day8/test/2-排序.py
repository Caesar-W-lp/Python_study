# 作者:李一安
# 2025年02月23日21时51分03秒
import random

# (新)快速排序
class Sort:

    def __init__(self, n):
        """
        n是参与排序的数字的数量
        :param n:
        """
        self.length = n  # 被排序的列表长度
        self.arr = [0] * n # 这里[]和[None]并不是一样的，[]空容器无法通过乘的方式来扩建
        self.random_data() # 初始化随机数组


    # 此函数为数组的初始化函数，用于生成随机数组
    def random_data(self):
        for i in range(self.length):
            self.arr[i] = random.randint(0, 99)


    # 打印数组
    def print_arr(self):
        print(self.arr)


    # 快速排序
    ## 找到分割值
    def partition(self, left, right):
        arr = self.arr
        k = i = left # i指针用于遍历，k指针用于排序

        # 随机选取一个元素作为分割值
        # 避免陷入最坏时间复杂度的措施
        random_pos = random.randint(left, right)
        arr[random_pos], arr[right] = arr[right], arr[random_pos]


        for i in range(left, right):
            if arr[i] < arr[right]: # 某个位置的值小于分割值，则将其与k指针交换
                arr[i], arr[k] = arr[k], arr[i]
                k += 1

        arr[right], arr[k] = arr[k], arr[right]

        return k



    def quick_sort(self, left, right):
        if left < right: # 递归停止条件
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)




    # 堆排
    # 调整某一个子树为大根堆
    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整为大根堆
        :param pos:被调整的元素位置，是父节点
        :param arr_len:当时列表的长度
        :return:
        """
        arr = self.arr

        dad = pos
        left_son = 2 * pos + 1
        right_son = 2 * pos + 2

        # 先默认左孩子为更大的孩子
        bigger_son = left_son

        while bigger_son < arr_len:

            # 判断右孩子存在且大于左孩子
            # 若有右孩子残缺则不进入
            if right_son < arr_len and arr[left_son] < arr[right_son]:
                bigger_son = right_son

            if arr[bigger_son] > arr[dad]:
                arr[bigger_son], arr[dad] = arr[dad], arr[bigger_son]

                # 当前的三角关系已经理清楚了，把父亲的头衔交给最大的儿子，对下一代的三角关系进行处理
                dad = bigger_son
                bigger_son = 2 * dad + 1
            else:
                break



    def heap_sort(self):

        # 列表堆调整为大根堆
        for current_dad in range(self.length // 2 - 1, -1, -1): # 列表在进行层次建树后，最后一个父节点的下标为 N//2-1，N为列表长度，最后一个父节点下标之前的下标全是父节点，这里是将所有的父节点下标逆序遍历
            self.adjust_max_heap(current_dad, self.length)

        # 进行堆排
        arr = self.arr

        # 堆顶节点与末节点交换位置
        arr[0], arr[self.length - 1] = arr[self.length - 1], arr[0]

        for arr_length in range(self.length - 1, 1, -1):
            self.adjust_max_heap(0, arr_length)
            arr[0], arr[arr_length - 1] = arr[arr_length - 1], arr[0]


if __name__ == '__main__':
    sort = Sort(10)
    sort.print_arr()

    print("快速排序")
    sort.quick_sort(0, sort.length - 1)
    sort.print_arr()


    print("堆排")
    sort.heap_sort()
    sort.print_arr()



# python中提供的排序sort和sorted的内核是归并排序