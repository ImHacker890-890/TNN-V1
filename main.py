import cv2
weights = [
  "YOUR_WEIGHTS_HERE
]
net = cv2.dnn.readNet(weights)
class Training:
  layer_name = net.getLayersName()
  output_layers = [layer_name[i[0] - 1] for i in net.getUnconnectedOutLayers()]
