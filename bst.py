def invert(self):
    self.left, self.right = (self.right, self.left)
    if self.left != None:
        self.left.invert()
    if self.right != None:
        self.right.invert()