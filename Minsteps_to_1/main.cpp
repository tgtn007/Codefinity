#include <iostream>

using namespace std;

int Minsteps_Memoization(int n, int *arr){
    if(n==1){
        arr[n]=0;
        return 0;
    }
    int x, y=INT_MAX, z=INT_MAX;
    if(arr[n-1]==-1){
        arr[n-1]=Minsteps_Memoization(n-1,arr);
        x=arr[n-1];
    }
    if(n%2==0){
        if(arr[n/2]==-1){
            arr[n/2]=Minsteps_Memoization(n/2,arr);
        }
        y=arr[n/2];
    }
    if(n%3==0){
        if(arr[n/3]==-1){
            arr[n/3]=Minsteps_Memoization(n/3,arr);
        }
    z=arr[n/3];
    }
    return min(x,min(y,z))+1;
}

int Minsteps(int n){
    if(n==1){
        return 0;
    }
    int x,y=INT_MAX, z=INT_MAX;
    x=Minsteps(n-1);
    if(n%2==0){
        y=Minsteps(n/2);
    }
    if(n%3==0){
        z=Minsteps(n/3);
    }
    int ans = min(x,min(y,z));
    return ans+1;
}

int main()
{
    int n;
    cin>>n;
    int *arr=new int[n+1];
    for(int i=0; i<=n; i++){
        arr[i]=-1;
    }
    cout<<"Minsteps to reach "<<n<<" with Memoization = "<<Minsteps_Memoization(n,arr)<<endl;
    cout<<"Minsteps to reach "<<n<<" with Brute Force = "<<Minsteps(n)<<endl;
    return 0;
}
