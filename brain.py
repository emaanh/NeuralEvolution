from nn import NN
# from alphabeta import AlphaBetaPruning

class Brain:
    def __init__(self, NNBool, oldNetwork = None):
        self.NNBool = NNBool
        self.nn = None
        self.alphaBeta = None
        # self.memory  
  
        if NNBool:
            if(oldNetwork == None):
                self.nn = NN([4,2])
            else:
                nn = oldNetwork
                # nn.doMutation()
        # else:
        # 	alphaBeat = AlphaBetaPruning()
   

   

    def doAction(self, inputs):
        if self.NNBool == True:
            # print("inputs: ", inputs)
            return self.nn.forwardProp(inputs)



