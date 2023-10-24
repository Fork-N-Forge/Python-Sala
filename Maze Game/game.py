import random

# Define the size of the maze
maze_width = 10
maze_height = 10

# Create the maze
maze = [["W" for _ in range(maze_width)] for _ in range(maze_height)]

# Function to generate a random maze using Randomized Prim's algorithm
def generate_random_maze():
    # Create a random starting point
    start_x = random.randint(1, maze_width - 2)
    start_y = random.randint(1, maze_height - 2)
    maze[start_y][start_x] = " "

    # List of directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Generate the maze using Randomized Prim's algorithm
    stack = [(start_x, start_y)]
    while stack:
        current_cell = stack.pop()
        x, y = current_cell

        # Shuffle the list of directions
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < maze_width - 1 and 0 < ny < maze_height - 1:
                if maze[ny][nx] == "W":
                    maze[ny][nx] = " "
                    stack.append((nx, ny))
                    maze[y + dy // 2][x + dx // 2] = " "

# Generate a random maze
generate_random_maze()

# Ensure there is a clear path from start to exit
maze[1][0] = " "
maze[maze_height - 2][maze_width - 1] = " "

# Add obstacles to the maze
for _ in range(10):  # You can adjust the number of obstacles
    obstacle_x = random.randint(1, maze_width - 2)
    obstacle_y = random.randint(1, maze_height - 2)
    maze[obstacle_y][obstacle_x] = "W"

# Initialize player position
player_x, player_y = 1, 1
maze[1][1] = "S"
maze[maze_height - 2][maze_width - 2] = "E"

# Game loop
while True:
    # Print the maze with the player's position marked by an emoji
    for row_idx, row in enumerate(maze):
        row_str = ""
        for col_idx, cell in enumerate(row):
            if row_idx == player_y and col_idx == player_x:
                row_str += "😀"  # Emoji to mark player's position
            else:
                row_str += cell
        print(row_str)

    # Check for game over or win
    if maze[player_y][player_x] == "E":
        print("Congratulations! You reached the exit. You win!")
        break
    elif maze[player_y][player_x] == "W":
        print("Game over! You hit a wall. You lose!")
        break

    # Get player input
    move = input("Enter 'W' to move up, 'S' to move down, 'A' to move left, or 'D' to move right: ").upper()

    # Move the player
    if move == "W" and player_y > 0 and maze[player_y - 1][player_x] != "W":
        player_y -= 1
    elif move == "S" and player_y < maze_height - 1 and maze[player_y + 1][player_x] != "W":
        player_y += 1
    elif move == "A" and player_x > 0 and maze[player_y][player_x - 1] != "W":
        player_x -= 1
    elif move == "D" and player_x < maze_width - 1 and maze[player_y][player_x + 1] != "W":
        player_x += 1
    else:
        print("Invalid move. Please try again.")

