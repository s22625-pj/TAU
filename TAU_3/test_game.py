import unittest
from unittest.mock import patch
from io import StringIO
from game import SimpleGame

class TestSimpleGame(unittest.TestCase):

    def test_generate_board(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Sprawdzenie, czy start, stop, przeszkody są poprawnie umieszczone na planszy
        self.assertEqual(game.board[game.start[0]][game.start[1]], 'A')
        self.assertEqual(game.board[game.stop[0]][game.stop[1]], 'B')
        for obstacle in game.obstacles:
            self.assertEqual(game.board[obstacle[0]][obstacle[1]], 'X')

    def test_display_board(self):
        game = SimpleGame(3, 3)
        game.generate_board()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            game.display_board()
            output = mock_stdout.getvalue().strip()

        # Sprawdzenie, czy plansza jest poprawnie wyświetlana na ekranie
        self.assertEqual(output, ' '.join([' ']*3) + '\n' + ' '.join([' ']*3) + '\n' + ' '.join([' ']*3))

    def test_move_success(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Ustawienie gracza w pozycji startowej
        game.current_pos = game.start

        # Przesunięcie gracza bez przeszkody
        result = game.move('right')

        # Sprawdzenie, czy ruch zakończył się sukcesem
        self.assertEqual(result, 'success')
        # Sprawdzenie, czy pozycja gracza została zaktualizowana
        self.assertEqual(game.current_pos, (game.start[0], game.start[1] + 1))

    def test_move_invalid(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Ustawienie gracza w pozycji startowej
        game.current_pos = game.start

        # Przesunięcie gracza poza planszę
        result = game.move('up')

        # Sprawdzenie, czy ruch zakończył się niepowodzeniem
        self.assertEqual(result, 'invalid_move')
        # Sprawdzenie, czy pozycja gracza pozostała bez zmian
        self.assertEqual(game.current_pos, game.start)

    def test_move_goal_reached(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Ustawienie gracza w pozycji tuż przed celem
        game.current_pos = (game.stop[0] - 1, game.stop[1])

        # Przesunięcie gracza na cel
        result = game.move('down')

        # Sprawdzenie, czy ruch zakończył się dotarciem do celu
        self.assertEqual(result, 'goal_reached')
        # Sprawdzenie, czy pozycja gracza została zaktualizowana
        self.assertEqual(game.current_pos, game.stop)

if __name__ == '__main__':
    unittest.main()
