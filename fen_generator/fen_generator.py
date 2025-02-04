class FENGenerator:
    def __init__(self, img):
        self.board_img = img
       
        self.class_to_FEN = {
            "white_pawn":'P',
            "white_knight": 'N',
            "white_bishop": 'B',
            "white_rook": 'R',
            "white_queen": 'Q',
            "white_king": 'K',
            "black_pawn":'p',
            "black_knight": 'n',
            "black_bishop": 'b',
            "black_rook": 'r',
            "black_queen": 'q',
            "black_king": 'k'
        }
    
    
    def crop_board_into_squares(self):
        
        height, width = self.board_img.shape[:2]

        # Ensure the board_img is square. If not, crop the central square region.
        if width != height:
            min_dim = min(width, height)
            start_x = (width - min_dim) // 2
            start_y = (height - min_dim) // 2
            self.board_img = self.board_img[start_y:start_y + min_dim, start_x:start_x + min_dim]
            height, width = self.board_img.shape[:2]
        
        # Calculate the size of each cell
        cell_size = width // 8  # since width == height after cropping
        
        # Create an 8x8 grid of squares
        squares = []
        for row in range(8):
            row_squares = []
            for col in range(8):
                x = col * cell_size
                y = row * cell_size
                square = self.board_img[y:y + cell_size, x:x + cell_size]
                # get coordinates of square x1, y1, x2, y2
                square_coords = [x, y, x + cell_size, y + cell_size]
                row_squares.append({"square": square, "coords": square_coords})
            squares.append(row_squares)
        
        return squares
    
    def generate_fen(self, detections, squares):
        
        fen_string = ""
        for row in range(8):
            current_empty_squares = 0
            for col in range(8):
                square_coords = squares[row][col]['coords']
                
                # check if any bbox_center in detections is inside the square_coords
                for detection in detections:
                    if detection['bbox_center'][0] >= square_coords[0] and detection['bbox_center'][0] < square_coords[2]:
                        if detection['bbox_center'][1] >= square_coords[1] and detection['bbox_center'][1] < square_coords[3]:
                            if current_empty_squares > 0:
                                fen_string += str(current_empty_squares)
                            current_empty_squares = 0
                            fen_string += self.class_to_FEN[detection['class']]
                            break
                else:
                    current_empty_squares += 1
                    
            if current_empty_squares > 0:
                fen_string += str(current_empty_squares)
            fen_string += "/"
            
        return fen_string[:-1]  # remove the last '/'











        

        

