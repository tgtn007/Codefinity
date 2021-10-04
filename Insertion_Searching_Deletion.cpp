#include<iostream>
#include<unordered_map> // T.c is O(1) for all kind of operation
// Using Seperate chaining technic. There is no fixed position for inserting key

#include<map> // It uses Self balancing tree or Red Black tree. T.c is O(log n)
//if we want to use key value in sorted order the we need map
using namespace std;

int main(){
    unordered_map<string, int> mpp;
    
    //Insertion Operation
    // 1st Method
    mpp["Raktim"]= 23;
    mpp["Soumi"] = 38;
    //2nd Method
    mpp.insert(make_pair("Rik",17));
    
    //Searching
    //1st Method
    auto f=mpp.find("Rik");
    if(f!=mpp.end()) cout<<"Rik no is "<<f ->second<<endl;
    else cout<<"Name not found"<<endl;
    //2nd Method
    if(mpp.count("Soumi")==true) cout<<"Soumi no is "<<mpp["Soumi"]<<endl;
    else cout<<"Name not found<<endl";
    
    //Deletion Operation
    mpp.erase("Rik");
    return 0;
}