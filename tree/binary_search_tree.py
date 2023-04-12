from binary_tree import BinaryTree

class BinarySearchTree(BinaryTree):

    def __init__(self, root):
        super().__init__(root)
        self.__binary_search_tree = self.get()
    
    def tree_search(self, node_current, node_target):
        if not node_current:
            return node_current
        if node_current == node_target:
            return node_current
        if node_target < node_current:
            return self.tree_search(self.__binary_search_tree[node_current]['left'], node_target)
        else:
            return self.tree_search(self.__binary_search_tree[node_current]['right'], node_target)
        
    def iterative_tree_search(self, node_current, node_target):
        while node_current and node_current != node_target:
            if node_target < node_current:
                node_current = self.__binary_search_tree[node_current]['left']
            else:
                node_current = self.__binary_search_tree[node_current]['right']
        return node_current
    
    def tree_min(self, root):
        while self.__binary_search_tree[root]['left'] is not None:
            root = self.__binary_search_tree[root]['left']
        return root
    
    def tree_max(self, root):
        while self.__binary_search_tree[root]['right'] is not None:
            root = self.__binary_search_tree[root]['right']
        return root

    def tree_successor(self, node):
        if self.__binary_search_tree[node]['right'] is not None:
            return self.tree_min(self.__binary_search_tree[node]['right'])
        parent = self.__binary_search_tree[node]['parent']
        while parent is not None and node == self.__binary_search_tree[parent]['right']:
            node = parent
            parent = self.__binary_search_tree[parent]['parent']
        return parent
    
    def tree_predecessor(self, node):
        if self.__binary_search_tree[node]['left'] is not None:
            return self.tree_max(self.__binary_search_tree[node]['left'])
        parent = self.__binary_search_tree[node]['parent']
        while parent is not None and node == self.__binary_search_tree[parent]['left']:
            node = parent
            parent = self.__binary_search_tree[parent]['parent']
        return parent
    
    def tree_insert(self, node):
        y = None
        x = self.get_root()
        while x is not None:
            y = x
            if node < x:
                x = self.__binary_search_tree[x]['left']
            else:
                x = self.__binary_search_tree[x]['right']
        self.__binary_search_tree[node] = {'parent': y, 'left': None, 'right': None}
        if y is not None and node < y:
            self.__binary_search_tree[y]['left'] = node
        else:
            self.__binary_search_tree[y]['right'] = node

    def __transplant(self, old, new):
        oldparent = self.__binary_search_tree[old]['parent']
        if oldparent == None:
            self.__binary_search_tree[new]['parent'] = None
            if self.__binary_search_tree[old]['left']:
                self.__binary_search_tree[new]['left'] = self.__binary_search_tree[old]['left']
            if self.__binary_search_tree[old]['right']:
                self.__binary_search_tree[new]['right'] = self.__binary_search_tree[old]['right']
        elif old == self.__binary_search_tree[oldparent]['left']:
            self.__binary_search_tree[oldparent]['left'] = new
        else:
            self.__binary_search_tree[oldparent]['right'] = new
            if new != None:
                self.__binary_search_tree[new]['parent'] = self.__binary_search_tree[old]['parent']
        del self.__binary_search_tree[old]

    def tree_delete(self, z):
        if not z in self.__binary_search_tree.keys():
            return None
        if not self.__binary_search_tree[z]['left']:
            self.__binary_search_tree[self.__binary_search_tree[z]['right']]['parent'] = self.__binary_search_tree[z]['parent']
            self.__transplant(z, self.__binary_search_tree[z]['right'])
        elif not self.__binary_search_tree[z]['right']:
            self.__binary_search_tree[self.__binary_search_tree[z]['left']]['parent'] = self.__binary_search_tree[z]['parent']
            self.__transplant(z, self.__binary_search_tree[z]['left'])
        else:
            y = self.tree_min(self.__binary_search_tree[z]['right'])
            if self.__binary_search_tree[y]['parent'] != z:
                self.__transplant(y, self.__binary_search_tree[y]['right'])
                self.__binary_search_tree[y]['right'] = self.__binary_search_tree[z]['right']
                self.__binary_search_tree[self.__binary_search_tree[y]['right']]['parent'] = y
            self.__transplant(z, y)
            self.__binary_search_tree[y]['left'] = self.__binary_search_tree[z]['left']
            self.__binary_search_tree[self.__binary_search_tree[y]['left']]['parent'] = y


def main():
    binary_search_tree = BinarySearchTree(root='6')
    binary_search_tree.add_child('6', '5', 'left')
    binary_search_tree.add_child('6', '7', 'right')
    binary_search_tree.add_child('5', '4', 'left')
    print(binary_search_tree.get())
    node = '6'
    target_node = '4'
    print( binary_search_tree.tree_search(node, target_node) )
    print( binary_search_tree.iterative_tree_search(node, target_node) )
    print('The minimum value of the subtree with root in %s is %s.' % (node, binary_search_tree.tree_min(node)))
    print('The maximum value of the subtree with root in %s is %s.' % (node, binary_search_tree.tree_max(node)))
    print('The successor of %s is %s.' % (node, binary_search_tree.tree_successor(node)))
    print('The predecessor of %s is %s.' % (node, binary_search_tree.tree_predecessor(node)))
    binary_search_tree.tree_insert('2')
    print(binary_search_tree.get())
    binary_search_tree.tree_delete('5')
    print(binary_search_tree.get())

if __name__ == '__main__':
    main()