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
    
    detector = Detector(model_path='model\\best.pt')

    detections = detector.detect(img)
    annotated_frame = detector.draw_annotations(img.copy(), detections)
    
    # once the new model is trained, crop the chessboard to only include the board and scale bboxes to fit the new crop
    
    FEN_generator = fen_generator.FENGenerator(img)
    squares = FEN_generator.crop_board_into_squares()
    
    # cv2.imshow('Annotated Frame', annotated_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # # Display all 8x8 squares as a chessboard
    # fig, axes = plt.subplots(8, 8, figsize=(20, 20))
    # for i in range(8):
    #     for j in range(8):
    #         # Convert each square from BGR to RGB for correct color display
    #         square_rgb = cv2.cvtColor(squares[i][j], cv2.COLOR_BGR2RGB)
    #         axes[i, j].imshow(square_rgb)
    #         axes[i, j].axis('off')
    #         axes[i, j].set_title(f'Row {i+1}, Col {j+1}')
    # plt.suptitle('Cropped Squares from Entire Board')
    # plt.tight_layout()
    # plt.show()
    
    fen = FEN_generator.generate_fen(detections, squares)
    print('FEN: \n%s' % fen)

if __name__ == "__main__":
    main()


