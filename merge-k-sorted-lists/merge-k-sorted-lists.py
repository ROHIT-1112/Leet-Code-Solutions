# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists and len(lists) == 0:
            return None
        while len(lists)>1:
            output = []
            
            for i in range(0,len(lists),2):
                list1 =lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                output.append(self.Merginglist(list1,list2))
                #print(output)
            lists = output
            #print("Final List :- ",output)
        return lists[0]
        
    def Merginglist(self,list1,list2):
        fake = ListNode()
        end = fake
        while list1 and list2:
            if list1.val < list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next = list2
                list2 = list2.next
            end = end.next
        if list1:
            end.next = list1
        elif list2:
            end.next = list2
        return fake.next
                