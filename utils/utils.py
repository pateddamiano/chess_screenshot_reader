import cv2

def read_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to read image from {image_path}")

    # resize image to at most 500 pixels in the longest dimension
    height, width = image.shape[:2]
    longest_side = max(height, width)
    scale_factor = 600 / longest_side
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    image = cv2.resize(image, (new_width, new_height))
    
    return image

def save_image(image, output_path):
    # Save the image using OpenCV
    cv2.imwrite(output_path, image)
    return True

def get_center_of_bbox(x1, y1, x2, y2):
    # Calculate the center of the bounding box
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    return center_x, center_y







