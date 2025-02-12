# Chess Screenshot Detection & FEN Generation
This repository implements a complete pipeline for detecting chess pieces and the chessboard in screenshots (e.g., from chess.com or lichess) and converting the detections into FEN notation. The project uses YOLO for object detection, a robust data augmentation pipeline to simulate real-world UI clutter (such as timers, text, and profile pictures), and post-processing code to split the detected board into 64 squares for FEN generation.

## Overview
The pipeline includes:

- YOLO-Based Detection
  * A YOLO model trained to detect both the chessboard (as one object) and individual chess pieces in cropped and full-screen images..
- Post-Processing & FEN Generation
  * Crop the board from a full screenshot using the predicted board bounding box.
  * Enforce a square board by center cropping.
  * Divide the cropped board into an 8×8 grid.
  * Map piece detections (with proper coordinate transformations) to chessboard squares and generate the final FEN string.
 
For training:
- Dataset Augmentation
  * Advanced augmentation techniques to simulate diverse real-world scenarios:
    + Randomly expand images to mimic various screenshot formats (vertical, horizontal, etc.).
    + Add noise and random backgrounds.
    + Overlay random UI elements such as timer text (MM:SS format) and small images (e.g., profile pictures)
- YOLO Label Generation
  * Scripts to generate YOLO-format annotation files (with normalized coordinates) for training, including labels for both the board and the pieces after augmentations.

# Repository Structure
```
chess-screenshot-detection/
├── YOLO_detection/
│   ├── data_model2.yaml             # YAML file for YOLO training parameters.
│   └── yolov5_training.ipynb        # Jupyter Notebook for training the model.
├── detector/
│   └── detector.py                  # Chess piece detector module.
├── experiments/
│   ├── square_cropping.ipynb        # Notebook for creating square splitting logic.
│   └── FEN_to_boundingBoxes.ipynb   # Notebook for creating augmnetations and creating YOLO bounding boxes for training and validation dataset
├── fen_generator/
│   └── fen_generator.py             # Module for generating the FEN notation from the detected pieces.
├── test_images/                     # Contains test images for the model.
├── utils/
│   └── utis.py                      # Module for reading and saving iamges, and bounding box utilities.
├── requirements.txt
└── main.py
```

## Installation
1. Clone the Repository.
2. Download the [model](https://huggingface.co/pdamiano/chess_screenshot_detection/tree/main) and create a ./model folder. Place the model in that folder. 
3. Set Up a Virtual Environment & Install Dependencies (`pip install -r requirements.txt`)
4. Use the trained model to predict the board bounding box from a full screenshot:

```
python main.py <path_to_screenshot>.png
```

## Future Work
- Further expand UI augmentation with additional elements (e.g., buttons, logos).
- Improve board detection in some challenging scenarios.
- Improve post-processing for rotated or perspective-tilted boards.










