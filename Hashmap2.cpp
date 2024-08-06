#include <iostream>
#include <list>
#include <vector>

using namespace std;

class SeparateChainingHashMap {
private:
    vector<list<pair<int, int>>> table;
    int capacity;
    int size;

    int hash(int key) {
        return key % capacity;
    }

public:
    SeparateChainingHashMap(int cap) : capacity(cap), size(0) {
        table.resize(capacity);
    }

    void insert(int key, int value) {
        int idx = hash(key);
        for (auto& kv : table[idx]) {
            if (kv.first == key) {
                kv.second = value;
                return;
            }
        }
        table[idx].push_back({key, value});
        size++;
    }

    bool find(int key) {
        int idx = hash(key);
        for (auto& kv : table[idx]) {
            if (kv.first == key) return true;
        }
        return false;
    }

    void remove(int key) {
        int idx = hash(key);
        table[idx].remove_if([key](const pair<int, int>& kv) { return kv.first == key; });
        size--;
    }
};
