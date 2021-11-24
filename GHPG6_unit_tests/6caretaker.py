 
class CareTaker:
    def __init__ (self, child, n):
        self.n = n
        self.child = child
        self.states = []
        self.index = -1
        self.label_for_redo = None

    def backup(self):
        if self.index < self.n-1 and self.index!=-1 and len(self.states) > self.index+1:
            for i in range(len(self.states)-self.index):
                self.states.pop()
        elif len(self.states)<self.n:
            pass
        else:
            self.states.pop(0)
            self.index -= 1
  
        self.states.append(self.child.save())
        self.index += 1

    def undo(self):
        if self.index<0:
            print('no states')
            return None
        memento = self.states[self.index]
        self.child.restore(memento)
        self.index -= 1
        self.label_for_redo = True

    def redo(self):
        if self.index>=self.n - 1 or self.index >= len(self.states)-1:
            print('no states to redo')
            return None
        if self.label_for_redo == True:
            self.index += 2
        else:
            self.index +=1
        memento = self.states[self.index]
        self.child.restore(memento)
        self.label_for_redo = False
        



    

    