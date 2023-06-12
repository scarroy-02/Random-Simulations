#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<pair<int,int>>> set_animals(int size){
    if(size == 1){
        vector<vector<pair<int,int>>> A = {{{0,0},{1,0}},{{0,0},{0,1}},{{0,0},{1,1}}};
        return A;
    }
    else{
        vector<vector<pair<int,int>>> A1;
        vector<vector<pair<int,int>>> A2;
        for(auto a : set_animals(size-1)){
            vector<pair<int,int>> eligible_moves;
            for(auto j : a){
                vector<pair<int,int>> moves = {{j.first,j.second+1},{j.first+1,j.second},{j.first+1,j.second+1}};
                for(auto k : moves){
                    if(find(a.begin(),a.end(),k) == a.end()){
                        eligible_moves.push_back(k);
                    }
                }
            }
            for(auto m : eligible_moves){
                vector<pair<int,int>> temp = a;
                temp.push_back(m);
                A1.push_back(temp);
            }
        }
        for(auto b : A1){
            sort(b.begin(),b.end());
            A2.push_back(b);
        }
        vector<vector<pair<int,int>>> res;
        for(auto x : A2){
            if(find(res.begin(),res.end(),x) == res.end()){
                res.push_back(x);
            }
        }
        return res;
    }
}

vector<vector<pair<int,int>>> re_set_animals(int size, int per){
    vector<vector<pair<int,int>>> A = set_animals(size);
    vector<vector<pair<int,int>>> A1;
    for(auto a : A){
        vector<pair<int,int>> adj_vert;
        for(auto j : a){
            vector<pair<int,int>> moves = {{j.first,j.second+1},{j.first+1,j.second},{j.first+1,j.second+1}};
            for(auto k : moves){
                if(find(a.begin(),a.end(),k) == a.end()){
                    adj_vert.push_back(k);
                }
            }
        }
        vector<vector<pair<int,int>>> res;
        for(auto x : adj_vert){
            if(find(res.begin(),res.end(),x) == res.end()){
                res.push_back(x);
            }
        }
        if(res.size() == per){
            A1.push_back(a);
        }
    }
    return A1;
}

int main(){
    vector<vector<pair<int,int>>> DA;
    cout << "re_set_animals(7,7):" << endl;
    DA = re_set_animals(7,7);
    for(auto a : DA){
        for(auto j : a){
            cout << "(" << j.first << "," << j.second << "),";
        }
        cout << endl;
    }
    for(int i=1; i<10; i++){
        for(int j=1; j<30; j++){
            DA = re_set_animals(i,j);
            cout << DA.size() << "," << i+1 << "," << j << endl;
        }
    }
    return 0;
}
