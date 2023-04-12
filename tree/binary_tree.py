class BinaryTree:

    def __init__(self, root):
        self.__binary_tree = dict()
        self.__add_root(root)

    def __add_root(self, node_name):
        self.__binary_tree[node_name] = {"parent": None, "left": None, "right": None}
    

    def get(self):
        return self.__binary_tree
    

    def add_child(self, parent, node_name, side):
        if parent in self.__binary_tree and not self.__binary_tree[parent][side]:
            self.__binary_tree[parent][side] = node_name
            self.__binary_tree[node_name] = {'parent': parent, 'left': None, 'right': None}

    def get_left(self, node_name):
        return self.__binary_tree[node_name]['left']
    
    def get_right(self, node_name):
        return self.__binary_tree[node_name]['right']
    
    def get_sibling(self, node_name):
        parent = self.__binary_tree[node_name]['parent']
        if node_name == self.__binary_tree[parent]['left']:
            return self.__binary_tree[parent]['right']
        else:
            return self.__binary_tree[parent]['left']
        
    def is_root(self, node_name):
        if not node_name in self.__binary_tree:
            raise Exception('Node is not in the tree')
        if not self.__binary_tree[node_name]['parent']:
            return True
        return False
    
    def is_leaf(self, node_name):
        if not node_name in self.__binary_tree:
            raise Exception('Node is not in the tree')
        return not self.__binary_tree[node_name]['left'] and not self.__binary_tree[node_name]['right']
    
    def get_children(self, node_name):
        children = list()
        if self.__binary_tree[node_name]['left']:
            children.append(self.__binary_tree[node_name]['left'])
        if self.__binary_tree[node_name]['right']:
            children.append(self.__binary_tree[node_name]['right'])
        return children
    
    def depth(self, node_name):
        if self.is_root(node_name):
            return 1
        return 1 + self.depth(self.__binary_tree[node_name]['parent'])
    
    def height(self, node_name):
        if self.is_leaf(node_name):
            return 0
        return 1 + max( self.height(child) for child in self.get_children(node_name) )


def main():
    binary_tree = BinaryTree()
    binary_tree.add_child('root', 'nodo1', 'left')
    binary_tree.add_child('root', 'nodo2', 'right')
    binary_tree.add_child('nodo1', 'nodo3', 'right')
    print(binary_tree.get())
    node = 'nodo1'
    print('Left child of %s is %s' % (node, binary_tree.get_left(node)))
    print('Right child of %s is %s' % (node, binary_tree.get_right(node)))
    print('Sibling of %s is %s' % (node, binary_tree.get_sibling(node)))
    print('Is %s the root: %s' % (node, binary_tree.is_root(node)))
    print('Is %s a leaf: %s' % (node, binary_tree.is_leaf(node)))
    print('The children of %s are: %s' % (node, binary_tree.get_children(node)))
    print('The depth of %s is: %s' % (node, binary_tree.depth(node)))
    print('The height of %s is: %s' % (node, binary_tree.height(node)))

if __name__ == '__main__':
    main()