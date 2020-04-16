// 更简单的做法：每次push的时候，都把最前面的元素挪到最后面就可以了...
//


#include <iostream>
#include <queue>

using namespace std;

#define aq (mq+1)%2

class MyStack {
private:
    queue<int> qs[2];
    int mq = 0;

public:
    /** Initialize your data structure here. */
    MyStack() {}

    /** Push element x onto stack. */
    void push(int x) {
        qs[mq].push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        while (qs[mq].size() != 1) {
            qs[aq].push(qs[mq].front());
            qs[mq].pop();
        }
        int res = qs[mq].front();
        qs[mq].pop();
        mq = aq;
        return res;
    }

    /** Get the top element. */
    int top() {
        while (qs[mq].size() != 1) {
            qs[aq].push(qs[mq].front());
            qs[mq].pop();
        }
        int res = qs[mq].front();
        qs[aq].push(res);
        qs[mq].pop();
        mq = aq;
        return res;
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return qs[mq].empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

int main() {
    MyStack s;
    s.push(1);
    s.push(2);
    s.top();
    s.pop();
    s.pop();
    cout << s.empty() << endl;

}