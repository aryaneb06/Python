#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int>arr={1,2,3,4,5};
    int target = 10;


    int flag = 0;

    for(int i=0;i<arr.size();i++)
    {
        if(target == arr[i]){
            cout<<"Found at "<<i;
            flag = 1;
            break;
        }
    }

    if(!flag){
        cout<<"Not Found"<<endl;
    }

    return 0;
}
