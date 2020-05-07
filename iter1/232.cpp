//
// Created by chenyufan on 2020/5/6.
//

#include <stack>

using namespace std;

class MyQueue {
    stack<int> s[2];
    int i = 0;
    bool isStack = true;

public:
    /** Push element x to the back of queue. */
    void push(int x) {
        if (!isStack) {
            while (!s[i].empty()) {
                int t = s[i].top();
                s[(i+1)%2].push(t);
                s[i].pop();
            }
            i = (i + 1) % 2;
            isStack = !isStack;
        }
        s[i].push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int x = peek();
        s[i].pop();
        return x;
    }

    /** Get the front element. */
    int peek() {
        if (!isStack) return s[i].top();
        while (!s[i].empty()) {
            int t = s[i].top();
            s[(i+1)%2].push(t);
            s[i].pop();
        }
        i = (i + 1) % 2;
        isStack = !isStack;
        return s[i].top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return s[i].empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */

int main() {

}
