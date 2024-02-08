#include <bits/stdc++.h>

using namespace std;

int N;

vector<pair<int,int>> lines;

vector<vector<int>> getInput() {
    cin >> N;
    vector<vector<int>> rtn;
    for(int i = 0; i < N; ++i) {
        int y , x1, x2;
        cin >> y >> x1 >> x2;
        rtn.push_back({y, x1 ,x2});
    }
    return rtn;
}

bool sortFunc(vector<int> vec1, vector<int> vec2) {
    if(vec1[0] != vec2[0])
        return vec1[0] < vec2[0];
    return vec1[1] < vec2[1];
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    vector<vector<int>> input = getInput();
    sort(input.begin(), input.end(), sortFunc);
    int ans = 0;
    int cur_y = 0;
    // cout << "\n==================\n";
    
    for(int i = 0; i < N; ++i) {
        for(auto it = lines.begin(); it != lines.end(); ++it) {
            if (input[i][1] >= it->first && input[i][1] <= it->second)
                input[i][1] = it->second;
            if (input[i][2] >= it->first && input[i][2] <it->second)
                input[i][2] = it->first;
        }
        if(input[i][1] < input[i][2])
            lines.push_back({input[i][1],input[i][2]});
    }
    cout << lines.size();
}