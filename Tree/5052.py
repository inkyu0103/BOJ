# 5052 Trie
import sys
input = sys.stdin.readline

class Node:
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):
        cur_node = self.head

        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node(s)

            cur_node = cur_node.children[s]

        cur_node.data = string

    def consist(self,string):
        # 검색을 하다가 data가 있네? 그게 자기와 다른 경우에는 ...
        cur_node = self.head

        for s in string:
            if cur_node.data:
                if cur_node.data != string:
                    return True
                else:
                    return False

            if cur_node.children[s]:
                cur_node = cur_node.children[s]








def sol():
    tc = int(input())
    for _ in range(tc):
        flag = 0
        trie = Trie()
        phone_num = int(input())
        phone_book = []
        for i in range(phone_num):
            number = input().strip()
            phone_book.append(number)
            trie.insert(number)

        for i in phone_book:
            if trie.consist(i):
                flag = 1
                print("NO")
                break

        if flag == 0:
            print("YES")

sol()

