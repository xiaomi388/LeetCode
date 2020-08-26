// BFS
// 注意点：反转函数写得太多bug了...

class Solution {
    int getBoardVal(vector<vector<int>>& board, int i) {
        int n = board.size();
        if (i > n*n || i <= 0) return -1;
        int row = n-(i-1)/n-1;
        int col = (n-row) % 2 ? (i-1) % n : n-(i-1)%n-1;
        //if (i == 17) cout << row << " " << col << endl;
        return board[row][col];
    }

public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        vector<int> visited(n*n+3);

        queue<int> q;

        q.push(1);
        int cost = 0;
        while (!q.empty()) {
            int qs = q.size();
            for (int i = 0; i < qs; ++i) {
                int s = q.front(); q.pop();
                //cout << s << endl;
                if (s == n*n) return cost;
                if (visited[s]) continue;
                visited[s] = 1;

                for (int j = 1; j <= 6; ++j) {
                    int ts = s+j;
                    if (ts > n*n) continue;

                    int bv = getBoardVal(board, ts);
                    //cout << "push: ";
                    if (bv != -1)  q.push(bv);//, cout << bv << endl;
                    else  q.push(ts);//, cout << ts << endl ;
                }
            }
            //cout << "----" << endl;
            cost++;
        }
        return -1;
    }
};

