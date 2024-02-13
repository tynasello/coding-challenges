/*
LeetCode 295
The median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value, and the median is the mean of the two
middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data
structure. double findMedian() returns the median of all elements so far.
Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling
findMedian. At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you
optimize your solution? If 99% of all integer numbers from the stream are in the
range [0, 100], how would you optimize your solution?
*/

#include <iostream>
#include <vector>

class PriorityQueue {

public:
  PriorityQueue(bool max_not_min) { this->max_not_min = max_not_min; }

  bool max_not_min;
  std::vector<int> heap;

  void swap(int i, int j) {
    int temp = this->heap[i];
    this->heap[i] = this->heap[j];
    this->heap[j] = temp;
  }

  void insert(int num) {
    this->heap.push_back(num);
    int i = this->get_size() - 1;
    if (max_not_min) {
      while (i > 0 && heap[i] > heap[(i - 1) / 2]) {
        this->swap(i, (i - 1) / 2);
        i = (i - 1) / 2;
      }
    } else {
      while (i > 0 && heap[i] < heap[(i - 1) / 2]) {
        this->swap(i, (i - 1) / 2);
        i = (i - 1) / 2;
      }
    }
  }

  void heapify(int i) {
    int extreme_i = i;
    int left_child_i = i * 2 + 1;
    int right_child_i = i * 2 + 2;

    if (this->max_not_min) {
      if (left_child_i < this->get_size() &&
          this->heap[left_child_i] > this->heap[extreme_i]) {
        extreme_i = left_child_i;
      }

      if (right_child_i < this->get_size() &&
          this->heap[right_child_i] > this->heap[extreme_i]) {
        extreme_i = right_child_i;
      }

      if (extreme_i != i) {
        this->swap(i, extreme_i);
        this->heapify(extreme_i);
      }

    } else {
      if (left_child_i < this->get_size() &&
          this->heap[left_child_i] < this->heap[extreme_i]) {
        extreme_i = left_child_i;
      }

      if (right_child_i < this->get_size() &&
          this->heap[right_child_i] < this->heap[extreme_i]) {
        extreme_i = right_child_i;
      }

      if (extreme_i != i) {
        this->swap(i, extreme_i);
        this->heapify(extreme_i);
      }
    }
  }

  int peek() const { return this->heap[0]; }

  int get_size() const { return this->heap.size(); }

  friend std::ostream &operator<<(std::ostream &os, const PriorityQueue &pq) {
    os << "[";
    for (size_t i = 0; i < pq.get_size(); ++i) {
      os << pq.heap[i];
      if (i != pq.get_size() - 1) {
        os << ", ";
      }
    }
    os << "]";
    return os;
  }
};

class MedianFinder {
public:
  // max heap holding values in the left of the sorted array
  PriorityQueue *lhs = new PriorityQueue(true);
  // min heap holding values in the right of the sorted array
  PriorityQueue *rhs = new PriorityQueue(false);

  MedianFinder() {}

  void addNum(int num) {
    int lhs_size = this->lhs->get_size();
    int rhs_size = this->rhs->get_size();

    if (lhs_size == rhs_size) {
      if (lhs_size == 0 || num < this->rhs->peek()) {
        this->lhs->insert(num);
      } else {
        this->rhs->insert(num);
      }
    } else {
      if (lhs_size > rhs_size) {
        if (num < this->lhs->peek()) {
          this->rhs->insert(this->lhs->peek());
          this->lhs->heap[0] = num;
          this->lhs->heapify(0);

        } else {
          this->rhs->insert(num);
        }
      } else {
        if (num > this->rhs->peek()) {
          this->lhs->insert(this->rhs->peek());
          this->rhs->heap[0] = num;
          this->rhs->heapify(0);
        } else {
          this->lhs->insert(num);
        }
      }
    }
  }

  double findMedian() {
    double median;
    int lhs_size = this->lhs->get_size();
    int rhs_size = this->rhs->get_size();
    if ((lhs_size + rhs_size) % 2 == 0) {
      median = (this->lhs->peek() + this->rhs->peek()) / 2.0;
    } else {
      if (lhs_size > rhs_size) {
        median = this->lhs->peek();
      } else {
        median = this->rhs->peek();
      }
    }
    return median;
  }
};

int main() {
  MedianFinder *obj = new MedianFinder();
  obj->addNum(1);
  obj->addNum(2);
  obj->addNum(3);
  double param_2 = obj->findMedian();

  std::cout << param_2 << std::endl;
}
