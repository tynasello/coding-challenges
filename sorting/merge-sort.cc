#include <iostream>
#include <vector>
using namespace std;

void printVec(const vector<int> v) {
  for (const int i : v) {
    cout << i << " ";
  }
  cout << endl;
}

void mergeSort(vector<int> &vec) {
  if (vec.size() == 1)
    return;

  int midi = vec.size() / 2;
  vector<int> lvec = {vec.begin(), vec.begin() + midi};
  vector<int> rvec = {vec.begin() + midi, vec.end()};

  mergeSort(lvec);
  mergeSort(rvec);

  auto lit = lvec.begin();
  auto rit = rvec.begin();

  for (int &i : vec) {
    if (lit == lvec.end()) {
      i = *rit;
      ++rit;
    } else if (rit == rvec.end()) {
      i = *lit;
      ++lit;
    } else if (*lit < *rit) {
      i = *lit;
      ++lit;
    } else {
      i = *rit;
      ++rit;
    }
  }
}

int main() {
  vector<int> vec = {-4, 38, 27, 0, 43, 4, -9, 9, 82, 10};
  printVec(vec);
  mergeSort(vec);
  printVec(vec);
}
