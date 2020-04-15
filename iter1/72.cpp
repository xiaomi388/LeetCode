// s[i,j] = min( s[i-1, j-1]+w1[i]==w2[j], s[i-1,j]+1, s[i, j-1]+1 )
// dp思想：当前状态的上一状态都有哪些？从每一种上一状态转移到当前状态，当前状态的值会怎么发生变化？

#include <string>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;


class Solution {
public:
    int minDistance(string word1, string word2) {
        int f[word1.length()+3][word2.length()+3];

        for (int i = 0; i <= word1.length(); ++i) f[i][0] = i;
        for (int i = 0; i <= word2.length(); ++i) f[0][i] = i;

        for (int i = 0; i < word1.length(); ++i) {
            for (int j = 0; j < word2.length(); ++j) {
                f[i+1][j+1] = min(f[i][j] + (int(word1[i] == word2[j])+1)%2, f[i+1][j] + 1);
                f[i+1][j+1] = min(f[i+1][j+1], f[i][j+1] + 1);
            }
        }

        return f[word1.length()][word2.length()];
    }
};


int main() {
    Solution s;
    auto res = s.minDistance("intention", "execution");
//    auto res = s.minDistance("horse", "ros");
    cout << res << endl;
}
