import numpy as np
import math 
import time
import os



def activation(x, method):
    if method == "relu":
        return(np.maximum(0,x))
    if method == "softmax":
        exp = np.exp(x)
        sig = np.sum(exp)
        return(np.divide(exp,sig))
    if method == "linear":
        return x
    if method == "weight_sigmoid":
        weight = 1/15
        sig = np.sum(exp)
        return(np.divide(1,1+np.exp(-np.divide(x,weight))))
    if method == "signed_dx_dy":
        x0 = x[0,0]
        x1 = x[1,0]
        if x0 == 0 and x1 == 0:
            print("well that fucking happened")
            retval = [0,0]
        elif abs(x0) > abs(x1):
            if(x0 > 0):
                retval = [1,0]
            else:
                retval = [-1,0]
        else:
            if(x1 > 0):
                retval = [0,1]
            else:
                retval = [0,-1]
        # print(retval)
        return np.array(retval)
        
        # if x[0,0] !=0 and x[1,0] != 0: #bug is here beause of int conversion
        #     if(abs(x[0,0])>abs(x[1,0])):
        #         r[0] = int(x[0,0]/abs(x[0,0]))
        #     else:
        #         r[1] = int(x[1,0]/abs(x[1,0]))
                
        # return np.array(r)

def normalize(features):
    # np.mean(features)
    # np.std(features)
    mean = [4,70,6,5,3,7,9,3,3]
    std_dev = [1,1,1,1,1,1,1,1,1]
    normalized_features = (np.subtract(features,mean)) / (std_dev)
    normalized_features = features
    
    return normalized_features, mean, std_dev
    
        
class NN: 
    def __init__(self, layers):
        self.layers = layers
        self.nL = len(layers) #number of layers
        if self.nL<2:
            raise Exception("Neural Network must have at least 2 layers")
        self.weights = [np.random.uniform(low=-1.0, high=1.0, size = (layers[i+1], layers[i])) for i in range(self.nL-1)]
        self.biases = [np.zeros((layer, 1)) for layer in layers[1:]]
        # self.biases = [np.random.uniform(low=-1.0, high=1.0, size = (layer, 1)) for layer in layers[1:]]
        # self.readWeights("06_08-50") 
        self.activations = ["linear" for L in layers[2:]] + ["signed_dx_dy"]
        
        # self.weights = [np.array([[-1,0,1,0],[0,-1,0,1]])]
    
    def randomizeWeights(self, weights):
        pass
    
    def readWeights(self, filename):
        # Construct the full path to the file
        path = os.path.join("Weights", filename)
        
        # Open and read the file
        with open(path, 'r') as file:
            # The first line specifies the architecture
            architecture = file.readline().strip().split(',')
            
            # Convert architecture to integer values
            architecture = [int(nodes) for nodes in architecture]
            
            # Validate or adjust the NN architecture if necessary
            # This step depends on how you want to handle mismatches between the file and the NN instance
            
            # Initialize an empty list to store the layers of weights
            self.weights = []
            
            # Since the weights for all nodes in a layer are on the same line, we iterate through the architecture
            for layer_idx in range(len(architecture) - 1):
                # Read the line for the current layer's weights
                weights_line = file.readline().strip()
                # Split the weights string into individual weights, filtering out any empty strings
                weights_str_list = [w for w in weights_line.split(',') if w]
                # Convert the strings to floats
                weights_float_list = [float(w) for w in weights_str_list]
                
                # Reshape the flat list of weights into a matrix based on the architecture
                layer_weights = np.array(weights_float_list).reshape(architecture[layer_idx + 1], architecture[layer_idx])
                
                # Append the matrix of weights for this layer to the self.weights list
                self.weights.append(layer_weights)

    def processStringWeights():
        pass
        
        
    
    def forwardProp(self, input):
        layers = len(self.weights)+1
        prevLayer = np.array(input).reshape(-1,1)
        for i in range(self.nL-1):
            prevLayer = np.matmul(self.weights[i], prevLayer) + self.biases[i]
            prevLayer = activation(prevLayer, self.activations[i])
        return prevLayer.flatten()
    
    #NOT FINISHED
    def backProp(self, output, correctIndex):
        cost = cost(output[correctIndex])
    
    def cost(self, n):
        return -math.log(n)
        
        
    #summary function is written with help of ChatGPT
    def summary(self):
        # Define the width of the box for formatting purposes
        box_width = 50

        # Function to create the top or bottom border of the box
        def create_border(width):
            return "+" + "-" * (width - 2) + "+"

        # Function to create a centered text line within the box
        def create_centered_line(text, width):
            text_length = len(text)
            side_space = (width - 2 - text_length) // 2
            return "|" + " " * side_space + text + " " * (width - 2 - text_length - side_space) + "|"

        # Function to create a left-aligned text line within the box
        def create_left_line(text, width):
            return "| " + text + " " * (width - 3 - len(text)) + "|"

        header_footer = create_border(box_width)
        header = create_centered_line("NEURAL NETWORK SUMMARY", box_width)

        summary_lines = [header_footer, header, header_footer]

        numWeights = sum(self.weights[i].size for i in range(self.nL-1))
        numBiases = sum(self.biases[i].size for i in range(self.nL-1))

        summary_lines.append(create_left_line(f"Number of Layers: {self.nL}", box_width))
        summary_lines.append(create_left_line(f"Number of Weights: {numWeights}", box_width))
        summary_lines.append(create_left_line(f"Number of Biases: {numBiases}", box_width))
        summary_lines.append(header_footer)  # Adding a separator

        # Calculate the maximum width needed for the layer info before "Activation"
        max_layer_info_width = max(len(f"L{i}: {self.layers[i]} Nodes") for i in range(self.nL))

        # summary_lines.append(create_left_line("Layer Configuration:", box_width))
        for i in range(self.nL):
            layer_info = f"L{i}: {self.layers[i]} Nodes".ljust(max_layer_info_width)
            if i > 0:  # Only add activation info if it's not the input layer
                layer_info += f" | Activation: {self.activations[i-1]}"
            summary_lines.append(create_left_line(layer_info, box_width))

        summary_lines.append(header_footer)  # Footer

        return "\n".join(summary_lines)



if __name__ == '__main__':
    features = [2, 2, 3, 2]
    nn = NN([len(features),2,2])
    print(nn.forwardProp(features))
    
    # for i in range(10000):
    #     nn = NN([len(features),2])
    #     c[tuple((nn.forwardProp(features)))] +=1
    
    
    
    
    # print(nn.summary())
    # c = {(1,0):0, (0,1):0, (-1, 0):0, (0,-1):0}
    # start = time.time()
    # for i in range(1000000):
    #     nn = NN([len(features),2])
    #     c[tuple((nn.forwardProp(features)))] +=1
    # end = time.time()
    
    # print(c)
    # print(end-start)
        

