#include <bits/stdc++.h>

using namespace std;

int N;

vector<vector<int>> lines;
vector<int> ys;

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

bool sortFuncRev(vector<int> vec1, vector<int> vec2) {
    // if(vec1[2] != vec2[2])
    //     return vec1[2] < vec2[2];
    return vec1[0] < vec2[0];
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
        auto a = input[i];
        for(auto it = lines.begin(); it != lines.end(); ++it) {
            if (input[i][1] >= (*it)[0] && input[i][1] <= (*it)[1])
                input[i][1] = (*it)[1];
            if (input[i][2] >= (*it)[0] && input[i][2] <= (*it)[1])
                input[i][2] = (*it)[0];
            if (input[i][1] >= input[i][2])
                break;
            if (input[i][1] == (*it)[1])
                (*it)[1] = input[i][2];
            if (input[i][2] == (*it)[0])
                (*it)[0] = input[i][1];
        }
        if(input[i][1] < input[i][2]){
            // cout << a[1] << " " << a[2] << " " << a[0] <<"\n";
            // cout << input[i][1] << " " << input[i][2] << " " << input[i][0] <<"\n";
            // cout << "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n";
            lines.push_back({input[i][1],input[i][2], input[i][0]});
            // cout<<lines.size() <<"\n";
            // for(int i = 0; i < lines.size(); ++i) {
            //     cout << lines[i][0] << " " << lines[i][1] << "\n";
            // }
            // cout << "\n\n==============\n\n";
            // ys.push_back(input[i][0]);
        }
    }
    // cout << "\n========================\n";
    // sort(lines.begin(),lines.end(),sortFuncRev);
    // cur_y = lines[0][2];
    // for(int i = 0; i < lines.size(); ++i) {
    //     cout << lines[i][0] << " " << lines[i][1] << " " << lines[i][2] << "\n";
    // }
    cout << lines.size();
}