import random

class SimpleGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.stop = None
        self.obstacles = set()
        self.current_pos = None

    def generate_board(self):
        # Losowanie startu i stopu przy krawędziach planszy
        self.start = (0, random.randint(0, self.cols - 1))
        self.stop = (self.rows - 1, random.randint(0, self.cols - 1))
        self.current_pos = self.start

        # Losowanie przeszkód
        num_obstacles = random.randint(1, min(self.rows, self.cols) // 2)
        for _ in range(num_obstacles):
            obstacle = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            while obstacle == self.start or obstacle == self.stop or obstacle in self.obstacles:
                obstacle = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            self.obstacles.add(obstacle)

        # Ustawienie startu, stopu i przeszkód na planszy
        self.board[self.start[0]][self.start[1]] = 'A'
        self.board[self.stop[0]][self.stop[1]] = 'B'
        for obstacle in self.obstacles:
            self.board[obstacle[0]][obstacle[1]] = 'X'

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def move(self, direction):
        new_pos = self.current_pos

        if direction == 'right':
            new_pos = (self.current_pos[0], self.current_pos[1] + 1)
        elif direction == 'left':
            new_pos = (self.current_pos[0], self.current_pos[1] - 1)
        elif direction == 'up':
            new_pos = (self.current_pos[0] - 1, self.current_pos[1])
        elif direction == 'down':
            new_pos = (self.current_pos[0] + 1, self.current_pos[1])

        # Sprawdzenie warunków ruchu
        if 0 <= new_pos[0] < self.rows and 0 <= new_pos[1] < self.cols and new_pos not in self.obstacles:
            self.board[self.current_pos[0]][self.current_pos[1]] = ' '
            self.current_pos = new_pos
            self.board[self.current_pos[0]][self.current_pos[1]] = 'A'

            # Sprawdzenie, czy gracz osiągnął cel
            if self.current_pos == self.stop:
                return 'goal_reached'
            return 'success'
        else:
            return 'invalid_move'


# Utworzenie gry i wygenerowanie planszy
game = SimpleGame(5, 5)
game.generate_board()
game.display_board()

# Manualne sterowanie ruchem
def main():
    while True:
        move_direction = input("Podaj kierunek ruchu (up/down/left/right): ")
        result = game.move(move_direction)

        if result == 'goal_reached':
            game.display_board()
            print("Gratulacje! Dotarłeś do celu.")
            break
        elif result == 'success':
            game.display_board()
        else:
            print("Niedozwolony ruch. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
