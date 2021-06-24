# TODO: Need to come back

class Maze(object):
    """docstring for Maze."""

    def __init__(self, maze_file_name):
        super(Maze, self).__init__()
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_file_name, 'r')
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
