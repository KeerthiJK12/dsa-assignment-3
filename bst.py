class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)

        return self._balance(node)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)

        return self._balance(node)

    def order_of_key(self, key):
        return self._order_of_key(self.root, key)

    def _order_of_key(self, node, key):
        if not node:
            return 0
        if key <= node.key:
            return self._order_of_key(node.left, key)
        else:
            return 1 + self._get_size(node.left) + self._order_of_key(node.right, key)

    def get_by_order(self, k):
        return self._get_by_order(self.root, k)

    def _get_by_order(self, node, k):
        if not node:
            return None
        left_size = self._get_size(node.left)
        if k < left_size:
            return self._get_by_order(node.left, k)
        elif k > left_size:
            return self._get_by_order(node.right, k - left_size - 1)
        else:
            return node.key

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_size(self, node):
        if not node:
            return 0
        return node.size

    def _balance(self, node):
        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance_factor < -1:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        z.size = 1 + self._get_size(z.left) + self._get_size(z.right)
        y.size = 1 + self._get_size(y.left) + self._get_size(y.right)

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        z.size = 1 + self._get_size(z.left) + self._get_size(z.right)
        y.size = 1 + self._get_size(y.left) + self._get_size(y.right)

        return y


avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
print(avl.find(20))  
print(avl.find(40))  
avl.remove(20)
print(avl.find(20))  
print(avl.order_of_key(25)) 
print(avl.get_by_order(1))  
