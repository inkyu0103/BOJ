#include<iostream>
#include<algorithm>
#include<set>

using namespace std;
int MIN = 10001;
int SUM = 0;

int main(){
    int start,end;
    set<int> Eratos;
    Eratos.insert(2);
    
    cin >> start >> end;
    
    for(int i=2;i<=10000;i++){
        Eratos.insert(i);
    }
    
    for(int i=2;i<=10000;i++){
        int j =2;
        while(i*j<=10000){
            if(Eratos.find(i*j)!=Eratos.end()){
                Eratos.erase(i*j);
            }
            j++;
        }
    
        
    }
    
    
    for(auto it = Eratos.begin();it != Eratos.end();it++){
        if(start<=*it && *it<=end){
            SUM += *it;
            MIN = min(MIN,*it);
            
        }
    }
    
    if(SUM){
        cout << SUM << "\n"<<MIN;
    }else{
        cout << -1;
    }
    
    return 0;
}
