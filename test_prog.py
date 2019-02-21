#!usr/local/bin/python


class TestProg:
    #Sort a given list
    # def sort_list(self, l1):
    #     t = len(l1)
    #     print sorted(l1)
    #     for i in range(t):
    #         for j in range(t-i-1):
    #             if l1[j] > l1[j+1]:
    #                 temp = l1[j+1]
    #                 l1[j+1] = l1[j]
    #                 l1[j] = temp
    #     print l1
    #
    # #Duplicate elements from list
    # def dup_ele(self,l2):
    #     l3 = []
    #     for i in l2:
    #         if i not in l3:
    #             l3.append(i)
    #     print l3

    def str_rev(self, ss):
        s1 = ''
        t = len(ss)
        for i in range(t):
            s1 += ss[t-i-1]
        print s1



obj = TestProg()
# obj.sort_list([10,1,45,6,9,-35,0])
# obj.dup_ele([10,1,45,6,9,1,1,45,6,10])
s = raw_input("Enter str:")
obj.str_rev(s)









