import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
from detector import Detector
from utils import read_image
from fen_generator import fen_generator


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        return
    
    img_path = sys.argv[1]
    img = read_image(img_path)
    
    detector = Detector(model_path='model\\screenshotReader_endToEnd_model2.pt')

    detections = detector.detect(img)
    annotated_frame = detector.draw_annotations(img.copy(), detections)
    
    FEN_generator = fen_generator.FENGenerator(img)
    squares = FEN_generator.crop_board_into_squares(detections)
    
    fen = FEN_generator.generate_fen(detections, squares)
    print('FEN: \n%s' % fen)

    cv2.imshow('Annotated Frame', annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()


