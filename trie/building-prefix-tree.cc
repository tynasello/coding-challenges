/*
LeetCode 208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously
inserted string word that has the prefix prefix, and false otherwise.
*/

#include <map>
#include <string>
using namespace std;

class Trie {
  class TrieNode {
  public:
    bool isTerminal;
    TrieNode *children[26];
    TrieNode() : isTerminal{false} {
      for (int i = 0; i < 26; i++)
        children[i] = nullptr;
    }
  };

  TrieNode *root;

public:
  Trie() : root{new TrieNode{}} {}

  void insert(string word) {
    TrieNode *curr = root;
    for (const char &c : word) {
      int i = c - 'a';
      if (!curr->children[i]) {
        curr->children[i] = new TrieNode{};
      }
      curr = curr->children[i];
    }
    curr->isTerminal = true;
  }

  bool search(string word) {
    TrieNode *curr = root;
    for (const char &c : word) {
      int i = c - 'a';
      if (!curr->children[i]) {
        return false;
      }
      curr = curr->children[i];
    }
    return curr->isTerminal ? true : false;
  }

  bool startsWith(string prefix) {
    TrieNode *curr = root;
    for (const char &c : prefix) {
      int i = c - 'a';
      if (!curr->children[i]) {
        return false;
      }
      curr = curr->children[i];
    }
    return true;
  }
};

/*
Alternate solution using hashmap for children

class Trie {
  struct TrieNode {
    bool isTerminal;
    map<char, TrieNode *> children;
  };

  TrieNode *root;

public:
  Trie() : root{new TrieNode{false, {}}} {}

  void insert(string word) {
    TrieNode *curr = root;
    for (const char &c : word) {
      if (curr->children.count(c) != 1) {
        curr->children[c] = new TrieNode{false, {}};
      }
      curr = curr->children[c];
    }
    curr->isTerminal = true;
  }

  bool search(string word) {
    TrieNode *curr = root;
    for (const char &c : word) {
      if (curr->children.count(c) != 1) {
        return false;
      }
      curr = curr->children[c];
    }
    return curr->isTerminal ? true : false;
  }

  bool startsWith(string prefix) {
    TrieNode *curr = root;
    for (const char &c : prefix) {
      if (curr->children.count(c) != 1) {
        return false;
      }
      curr = curr->children[c];
    }
    return true;
  }
};
*/
