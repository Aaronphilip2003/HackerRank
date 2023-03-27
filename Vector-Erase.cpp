#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector<int> v1;
    int n;
    cin>>n;
    int ele;
    for(int i=0;i<n;i++)
    {
        cin>>ele;
        v1.push_back(ele);   
    }
    int single_pos=0;
    cin>>single_pos;
    int a,b;
    cin>>a>>b;
    v1.erase(v1.begin()+single_pos);
    v1.erase(v1.begin()+(a-1),v1.begin()+(b-1));
    cout<<v1.size()<<endl;
    for(int i=0;i<v1.size();i++)
    {
        cout<<v1[i]<<" ";
    }
    return 0;
}
