#include <iostream>
#include<bits/stdc++.h>


using namespace std;

vector<int> MaxMin(vector<int>&v,int start,int end,int mx=INT_MIN,int mn=INT_MAX){
        if(start == end)return{v[start],v[end]};
        if(start+1 == end){
            mx = max(v[start],v[end]);
            mn = min(v[start],v[end]);
        }
        else{
            int mid = (start+end)/2;
            vector<int> l = MaxMin(v,start,mid,mx,mn);
            vector<int> r = MaxMin(v,mid+1,end,mx,mn);
            mx  = max(l[0],r[0]);
            mn = min(l[1],r[1]);
        }
        return {mx,mn};
}



int main() {
    vector<int>v,ans;
    v = {3,45,2,14,12,43,24,56,21,6,8,8};
    ans = MaxMin(v,0,v.size()-1);
    cout<<"Max: "<<ans[0]<<endl
        <<"Min: "<<ans[1]<<endl;
        return 0;
}