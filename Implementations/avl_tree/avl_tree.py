"""A pointer-based AVL tree."""


class AVLTree:
    def __init__(self, item, parent=None, height=0):
        self.item = item
        self.left = None
        self.right = None
        self.height = height
        self.parent = parent

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self.item
        if self.right is not None:
            yield from self.right

    def leftRotate(self):
        s = self
        sr = self.right
        srl = self.right.left

        root_parent = s.parent  
        new_root = sr
        new_root.parent = root_parent
        new_root.left = s
        new_root.left.parent = new_root
        new_root.left.right = srl
        if srl is not None:
            srl.parent = new_root.left

        s._update_height()
        new_root._update_height()
        return new_root

    def rightRotate(self):
        s = self
        sl = self.left
        slr = self.left.right

        root_parent = s.parent
        new_root = sl
        new_root.right = s
        s.parent = new_root
        new_root.parent = root_parent
        s.left = slr
        if slr is not None:
            slr.parent = s

        self._update_height()
        new_root._update_height()
        return new_root

    def rightLeftRotate(self):
        s = self
        sr = self.right
        s.right = sr.rightRotate()
        new_root = s.leftRotate()


        return new_root

    def leftRightRotate(self):
        s = self
        sl = s.left
        s.left = sl.leftRotate()
        new_root = s.rightRotate()

        return new_root

    def _update_height(self):
        if self.left is None:
            left_height = -1
        else:
            left_height = self.left.height

        if self.right is None:
            right_height = -1
        else:
            right_height = self.right.height

        self.height = 1 + max(left_height, right_height)

        if self.parent is not None:
            self.parent._update_height()
            
        return

    def _balance_factor(self):
        if self.height == 0:
            return 0

        if self.left is None:
            left_height = -1
        else:
            left_height = self.left.height

        if self.right is None:
            right_height = -1
        else:
            right_height = self.right.height

        balance_factor = left_height - right_height
        return balance_factor

    def rebalance(self):
        needs_leftRotation = False
        if self._balance_factor() == -2 and (self.right._balance_factor() == -1 or self.right._balance_factor() == 0) :
            needs_leftRotation = True

        needs_rightRotation = False
        if self._balance_factor() == 2 and (self.left._balance_factor() == 1 or self.left._balance_factor() == 0) :
            needs_rightRotation = True

        needs_leftRightRotation = False
        if self._balance_factor() == 2 and self.left._balance_factor() == -1:
            needs_leftRightRotation = True

        needs_rightLeftRotation = False
        if self._balance_factor() == -2 and self.right._balance_factor() == 1:
            needs_rightLeftRotation = True

        parent = self.parent
        rotation = False
        node = self

        if (needs_leftRotation):
            print("LEFT ROTATION")
            node = self.leftRotate()
            rotation = True

        elif (needs_rightRotation):
            print("RIGHT ROTATION")
            node = self.rightRotate()
            rotation = True

        elif (needs_leftRightRotation):
            print("LEFT-RIGHT ROTATION")
            node = self.leftRightRotate()
            rotation = True

        elif (needs_rightLeftRotation):
            print("RIGHT-LEFT ROTATION")
            node = self.rightLeftRotate()
            rotation = True

        if parent is not None:
            if rotation:

                if node.parent.item > node.item:
                    parent.left = node
                else:
                    parent.right = node

            return self.parent.rebalance()
        else:
            return node

    def _parent_search(self, x):
        if self is None:
            return None
        if self.item == x:
            return self
        if self.item > x:
            temp = AVLTree._parent_search(self.left, x)
        else:
            temp = AVLTree._parent_search(self.right, x)
        if temp is None:
            return self
        return temp

    def search(self, x):
        if self is None:
            return None
        if self.item == x:
            return self
        if self.item > x:
            return AVLTree.search(self.left, x)
        return AVLTree.search(self.right, x)

    def _get_min(self):
        if self.left is None:
            return self
        return self.left._get_min()

    def get_successor(self):
        if self.right is None:
            return None
        return self.right._get_min()

    def insert(self, x):
        parent_node = self._parent_search(x)

        new_node = AVLTree(x, parent=parent_node)

        if x > parent_node.item:
            parent_node.right = new_node
        else:
            parent_node.left = new_node

        new_node._update_height()

        new_root =  new_node.rebalance()

        return new_root

    def delete(self, x):
        n = self.search(x)

        if n is None:
            return self

        elif n.height == 0:
            if n.parent is None:
                return None

            if n.item < n.parent.item:
                n.parent.left = None
            else:
                n.parent.right = None

        elif n.left is not None and n.right is None:
            n.left.parent = n.parent
            if n.parent is None:
                return n.left
            if n.parent.item < n.item:
                n.parent.right = n.left
            else:
                n.parent.left = n.left
            

        elif n.left is None and n.right is not None:
            n.right.parent = n.parent
            if n.parent is None:
                return n.right

            if n.item < n.parent.item:
                n.parent.left = n.right
            else:
                n.parent.right = n.right
        else:
            if n.right is not None:
                succesor = n.get_successor()
                if succesor != n.right:
                    n.item = succesor.item
                    succesor.parent.left = succesor.right  
                    if succesor.right is not None:
                        succesor.right.parent = succesor.parent
                    
                else:
                    n.item = succesor.item
                    n.right = succesor.right
                    if succesor.right is not None:
                        n.right.parent = n
            

        n._update_height()

        return n.rebalance()
