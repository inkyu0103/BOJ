#include<iostream>
using namespace std;


int main(){
    int N ;
    cin >> N;
    if(N==1) return 0;
    
    
    while(N!=1){
        for(int i=2;;i++){
            if(N%i == 0){
                N = N/i;
                cout <<i<<"\n";
                break;
            }
        }
    }
        
    return 0;
}

