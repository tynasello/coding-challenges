/*
LeetCode 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You
may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
  vector<vector<string>> sols;
  vector<bool> cols;
  vector<bool> diagRightToLeft;
  // col + row
  // 2 3 4 5
  // 3 4 5 6
  // 4 5 6 7
  // 5 6 7 8
  vector<bool> diagLeftToRight;
  // col - row
  // 0  1  2  3
  // -1 0  1  2
  // -2 -1 0  1
  // -3 -2 -1 0

public:
  void search(vector<string> &board, int row, int n) {
    if (row == n) {
      sols.emplace_back(board);
      return;
    }
    for (int col = 0; col < n; ++col) {
      if (cols[col] || diagRightToLeft[row + col] ||
          diagLeftToRight[col - row + n - 1]) {
        continue;
      }
      cols[col] = diagRightToLeft[row + col] =
          diagLeftToRight[col - row + n - 1] = 1;
      board[row][col] = 'Q';
      search(board, row + 1, n);
      cols[col] = diagRightToLeft[row + col] =
          diagLeftToRight[col - row + n - 1] = 0;
      board[row][col] = '.';
    }
  }

  vector<vector<string>> solveNQueens(int n) {
    cols = vector<bool>(n, false);
    diagRightToLeft = vector<bool>(n, false);
    diagLeftToRight = vector<bool>(n, false);
    vector<string> board;
    for (int i = 0; i < n; ++i) {
      string row = "";
      for (int j = 0; j < n; ++j) {
        row += ".";
      }
      board.emplace_back(row);
    }
    search(board, 0, n);
    return sols;
  }
};
