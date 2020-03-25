//
// Created by chenyufan on 2020/3/25.
//

#include <stack>
#include <iostream>

using namespace std;

class MinStack {

    stack<int> minStack;
    stack<int> itnStack;

public:
    /** initialize your data structure here. */
    MinStack() {
        minStack = stack<int>();
        itnStack = stack<int>();
    }

    void push(int x) {
        itnStack.push(x);
        int min = minStack.empty() ? INT_MAX : minStack.top();
        if (x <= min) {
            minStack.push(x);
        }
    }

    void pop() {
        int top = itnStack.top();
        itnStack.pop();
        if (top == minStack.top()) {
            minStack.pop();
        }
    }

    int top() {
        return itnStack.top();
    }

    int getMin() {
        return minStack.top();
    }
};

int main() {
    MinStack s;
    s.push(-2);
    s.push(0);
    s.push(-3);
    cout << s.getMin() << endl;
    s.pop();
    cout << s.top() << endl;


}


/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */