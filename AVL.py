class Tree:

    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right

        newleft = Tree(v)
        newleft.left = tl
        newleft.right = trl

        self.value = vr
        self.right = trr
        self.left - newleft
        return
    
    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tll = self.left.left
        tlr = self.left.right
        tr = self.right

        newright = Tree(v)
        newright.left = tlr
        newright.right = tr

        self.value = vl
        self.left = tll
        self.right = newright
        return

    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()

        if self.value == v:
            return

        if v < self.value:
            self.left.insert(v)
            self.left.rebalance()
            return

        if v > self.value:
            self.right.insert(v)
            self.right.rebalance()
            return

    def rebalance(self):
        if self.left.height() - self.right.height() > 1:
            if self.left.left.height() > self.left.right.height():
                self.left.left.leftrotate()
                self.rightrotate()
            else:
                self.left.right.rightrotate()
                self.leftrotate()
        elif self.right.height() - self.left.height() > 1:
            if self.right.right.height() > self.right.left.height():
                self.right.right.rightrotate()
                self.leftrotate()
            else:
                self.right.left.leftrotate()
                self.rightrotate()
        return

    def isempty(self): 
        return self.value == None

    def height(self):
        if self.isempty():
            return 0
        else:
            return max(self.left.height(),self.right.height()) + 1

