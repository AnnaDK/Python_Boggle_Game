def make_grid(width, height):
    """
    Creates a grid that will hold all the tiles for a boggle
    """
    return{(row, col): ' ' for row in range(height)
        for col in range(width)
    }
    