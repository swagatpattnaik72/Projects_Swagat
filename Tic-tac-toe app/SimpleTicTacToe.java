import java.util.*;

public class SimpleTicTacToe {

    static char[][] board = new char[4][4];
    static Scanner sc = new Scanner(System.in);
    static Random rand = new Random();

    public static void main(String[] args) {

        // Initialize board with spaces
        for (char[] row : board)
            Arrays.fill(row, ' ');

        // Main game loop
        while (true) {

            playerTurn();

            if (checkWin('X')) {
                printBoard();
                System.out.println("Player wins!");
                break;
            }

            if (isFull()) {
                printBoard();
                System.out.println("It's a draw!");
                break;
            }

            computerTurn();

            if (checkWin('O')) {
                printBoard();
                System.out.println("Computer wins!");
                break;
            }

            if (isFull()) {
                printBoard();
                System.out.println("It's a draw!");
                break;
            }
        }
    }

    static void printBoard() {
        System.out.println("-------------");
        for (char[] row : board) {
            System.out.print("|");
            for (char c : row)
                System.out.print(c + "|");
            System.out.println("\n-------------");
        }
    }

    static void playerTurn() {
        printBoard();
        int r, c;
        while (true) {
            System.out.print("Enter row and column (1-4): ");
            r = sc.nextInt() - 1;
            c = sc.nextInt() - 1;

            if (r >= 0 && r < 4 && c >= 0 && c < 4 && board[r][c] == ' ') {
                board[r][c] = 'X';
                break;
            } else {
                System.out.println("Invalid move! Try again.");
            }
        }
    }

    static void computerTurn() {
        int r, c;
        do {
            r = rand.nextInt(4);
            c = rand.nextInt(4);
        } while (board[r][c] != ' ');

        board[r][c] = 'O';
        System.out.println("Computer chose: " + (r + 1) + "," + (c + 1));
    }

    static boolean checkWin(char p) {
        for (int i = 0; i < 4; i++) {
            if (all(p, board[i][0], board[i][1], board[i][2], board[i][3]) ||  // rows
                all(p, board[0][i], board[1][i], board[2][i], board[3][i]))    // columns
                return true;
        }
        return all(p, board[0][0], board[1][1], board[2][2], board[3][3]) ||   // diagonal \
               all(p, board[0][3], board[1][2], board[2][1], board[3][0]);     // diagonal /
    }

    static boolean all(char p, char... cells) {
        for (char c : cells)
            if (c != p)
                return false;
        return true;
    }

    static boolean isFull() {
        for (char[] row : board)
            for (char c : row)
                if (c == ' ')
                    return false;
        return true;
    }
}
