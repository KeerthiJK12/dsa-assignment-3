#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

struct Node {
    int key, height, size;
    Node *left, *right;
    Node(int k) : key(k), height(1), size(1), left(nullptr), right(nullptr) {}
};

class AVLTree {
private:
    Node* root;

    int height(Node* node) {
        return node ? node->height : 0;
    }

    int size(Node* node) {
        return node ? node->size : 0;
    }

    int balanceFactor(Node* node) {
        return height(node->left) - height(node->right);
    }

    Node* rightRotate(Node* y) {
        Node* x = y->left;
        Node* T2 = x->right;

        x->right = y;
        y->left = T2;

        y->height = max(height(y->left), height(y->right)) + 1;
        x->height = max(height(x->left), height(x->right)) + 1;

        y->size = size(y->left) + size(y->right) + 1;
        x->size = size(x->left) + size(x->right) + 1;

        return x;
    }

    Node* leftRotate(Node* x) {
        Node* y = x->right;
        Node* T2 = y->left;

        y->left = x;
        x->right = T2;

        x->height = max(height(x->left), height(x->right)) + 1;
        y->height = max(height(y->left), height(y->right)) + 1;

        x->size = size(x->left) + size(x->right) + 1;
        y->size = size(y->left) + size(y->right) + 1;

        return y;
    }

    Node* insert(Node* node, int key) {
        if (!node) return new Node(key);

        if (key < node->key)
            node->left = insert(node->left, key);
        else if (key > node->key)
            node->right = insert(node->right, key);
        else
            return node;

        node->height = max(height(node->left), height(node->right)) + 1;
        node->size = size(node->left) + size(node->right) + 1;

        int balance = balanceFactor(node);

        if (balance > 1 && key < node->left->key)
            return rightRotate(node);

        if (balance < -1 && key > node->right->key)
            return leftRotate(node);

        if (balance > 1 && key > node->left->key) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }

        if (balance < -1 && key < node->right->key) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }

        return node;
    }

    Node* minNode(Node* node) {
        Node* current = node;
        while (current->left != nullptr)
            current = current->left;
        return current;
    }

    Node* remove(Node* node, int key) {
        if (!node) return node;

        if (key < node->key)
            node->left = remove(node->left, key);
        else if (key > node->key)
            node->right = remove(node->right, key);
        else {
            if (!node->left)
                return node->right;
            else if (!node->right)
                return node->left;

            Node* temp = minNode(node->right);
            node->key = temp->key;
            node->right = remove(node->right, temp->key);
        }

        node->height = max(height(node->left), height(node->right)) + 1;
        node->size = size(node->left) + size(node->right) + 1;

        int balance = balanceFactor(node);

        if (balance > 1 && balanceFactor(node->left) >= 0)
            return rightRotate(node);

        if (balance > 1 && balanceFactor(node->left) < 0) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }

        if (balance < -1 && balanceFactor(node->right) <= 0)
            return leftRotate(node);

        if (balance < -1 && balanceFactor(node->right) > 0) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }

        return node;
    }

    bool find(Node* node, int key) {
        if (!node) return false;
        if (node->key == key) return true;
        if (key < node->key) return find(node->left, key);
        else return find(node->right, key);
    }

    int orderOfKey(Node* node, int key) {
        if (!node) return 0;
        if (key <= node->key) return orderOfKey(node->left, key);
        else return size(node->left) + 1 + orderOfKey(node->right, key);
    }

    int getByOrder(Node* node, int k) {
        if (!node) return -1;
        int leftSize = size(node->left);
        if (k <= leftSize) return getByOrder(node->left, k);
        else if (k == leftSize + 1) return node->key;
        else return getByOrder(node->right, k - leftSize - 1);
    }

    void destroy(Node* node) {
        if (node) {
            destroy(node->left);
            destroy(node->right);
            delete node;
        }
    }

public:
    AVLTree() : root(nullptr) {}

    ~AVLTree() {
        destroy(root);
    }

    void insert(int key) {
        root = insert(root, key);
    }

    void remove(int key) {
        root = remove(root, key);
    }

    bool find(int key) {
        return find(root, key);
    }

    int orderOfKey(int key) {
        return orderOfKey(root, key);
    }

    int getByOrder(int k) {
        return getByOrder(root, k);
    }
};
