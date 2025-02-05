from ultralytics import YOLO
import cv2
import numpy as np
import sys
sys.path.append('..')  
from utils import get_center_of_bbox


class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        
    def detect(self, frame):
        """
        Detect objects in a given frame using the trained model.

        Args:
            frame: The input frame (numpy array) to perform object detection on.

        Returns:
            A list of dictionaries containing information about detected objects.
                Each dictionary has the following keys:
                    - 'class': The class name of the detected object.
                    - 'confidence': The confidence score of the detection.
                    - 'bbox': A tuple representing the bounding box coordinates (x1, y1, x2, y2).

        Notes:
            This method uses the trained model to generate predictions for the input frame.
            The resulting detections are then converted into a list of dictionaries for easier processing and analysis.
        """
        
        results = self.model.predict(frame, conf=0.8)
        cls_names = results[0].names

        detections = []
        boxes = results[0].boxes.xyxy.tolist()
        scores = results[0].boxes.conf.tolist()
        classes = results[0].boxes.cls.tolist()
        
        if 12.0 not in classes:
            print("Could not find board in image.")
            quit()
        
        for box, score, cls in zip(boxes, scores, classes):
            x1, y1, x2, y2 = box
            detections.append({
                'class': cls_names[cls],
                'confidence': score,
                'bbox': (x1, y1, x2, y2),
                'bbox_center': get_center_of_bbox(x1, y1, x2, y2)
            })
            
        if len(detections) == 0:
            print("No detections found.")
            return []

        return detections

    def draw_annotations(self, frame, detections):
        """
        Draws bounding boxes and labels around detected objects in the given image.

        Args:
            frame (numpy.ndarray): The input image.
            detections (list[dict]): A list of dictionaries containing detection information,
                each dictionary having the following keys:
                    - 'class' (str): The class name of the detected object.
                    - 'confidence' (float): The confidence score of the detection.
                    - 'bbox' (tuple[float, float, float, float]): The bounding box coordinates
                        in the format (x1, y1, x2, y2).

        Returns:
            numpy.ndarray: The input image with bounding boxes and labels drawn around detected objects.

        Note:
            This function assumes that the detection dictionary keys match the expected structure.
        """
        for detection in detections:
            class_name = detection['class']
            confidence = detection['confidence']
            bbox = detection['bbox']
            # convert bbox to all ints in place
            x1, y1, x2, y2 = map(int, bbox)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{class_name}: {confidence:.2f}', (x1, y1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)
            # draw a circle at the center of the bounding box
            x, y = get_center_of_bbox(x1, y1, x2, y2)
            cv2.circle(frame, (int(x), int(y)), 3, (0, 0, 255), -1)
            
        return frame
    





