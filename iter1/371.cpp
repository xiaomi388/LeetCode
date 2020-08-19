// 技巧：一位一位来加。记得最后一位要判断下，直接丢弃溢出的值。
//


class Solution {
    void printBit(int a) {
        for (int i = 31; i >=0 ; --i) {
            if ((1 << i) & ans) cout << 1;
            else cout << 0;
        }
        cout << endl;
    }
public:
    int getSum(int a, int b) {
        int ans = 0;
        for (int i = 0; i < 32; ++i) {
            int x = (1 << i);
            if ((x & a) && (x & b)) {
                if (i+1 <= 31) {
                    ans = (ans | (1 << (i+1)));
                }
                if (!(x & ans)) {
                    ans = (ans & (~x));
                }
            } else if (!(x&a) && !(x&b)) {
                continue;
            } else {
                if (i == 31) {
                    printBit(ans);
                }
                if (x & ans) {
                    if (i+1 <= 31) {
                        ans = (ans | (1 << (i+1)));
                    }
                    ans = (ans & (~x));
                } else {
                    ans = (ans | x);
                }
            }
        }
        printBit(ans);
        return ans;
    }
};
