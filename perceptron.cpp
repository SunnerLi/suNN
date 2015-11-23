#include<iostream>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cstdio>
using namespace std;

double weight[20][20];//bit_out  bit_in

void build(){
    for(int i=0;i<20;i++)
        for(int j=0;j<20;j++)
            weight[i][j]=(rand()%101-50)*0.01;//-0.50~0.50
}
int Case,bit_in,bit_out;
int input[20][20],test[20];//case bit
int output[20][20];//case bit
int ans[20];//tmp bit
double T,L;
int main(){
    srand(time(NULL));
    build();
    cout<<"How many cases           : ";cin>>Case;
    cout<<"How many bits of input   : ";cin>>bit_in;
    cout<<"Enter input :"<<endl;
    for(int i=0;i<Case;i++)
        for(int j=0;j<bit_in;j++)
            cin>>input[i][j];
    cout<<"How many bits of output  : ";cin>>bit_out;
    cout<<"Enter output :"<<endl;
    for(int i=0;i<Case;i++)
        for(int j=0;j<bit_out;j++)
            cin>>output[i][j];
    cout<<"Enter threshold'T' : ";cin>>T;
    cout<<"Enter learning rate : ";cin>>L;
    int cnt=0,RE=0;
    bool c=true,cant=true;
    for(int x=0;x<bit_out;x++){
        c=true;
        while(c&&cant){
            cnt++;
            if(cnt==2000){build();RE++;cout<<".";cnt%=2000;}
            if(RE>20)cant=false;
            c=false;
            for(int i=0;i<Case;i++){
                int ANS=0;
                double s=0;
                for(int j=0;j<bit_in;j++)
                    s+=weight[x][j]*input[i][j];
                ANS=((s>T)?1:0);
                if(ANS!=output[i][x]){//update
                    c=true;
                    for(int j=0;j<bit_in;j++)
                        weight[x][j]+=L*(output[i][x]-ANS)*input[i][j];
                }
            }
        }

    }
    cout<<endl;
    if(!cant)cout<<"can't learn"<<endl;
    else{
    for(int x=0;x<bit_out;x++){
        cout<<"the weight of "<<x<<" bit is:"<<endl;
        for(int j=0;j<bit_in;j++){
            printf("%8.2f",weight[x][j]);
        }
        cout<<endl;
    }
    while(1){
        cout<<"Enter test case : ";
        for(int i=0;i<bit_in;i++)cin>>test[i];
        cout<<"the answer is:"<<endl;
        for(int x=0;x<bit_out;x++){
            double s=0;
            for(int j=0;j<bit_in;j++)
                s+=test[j]*weight[x][j];
            cout<<(s>T?1:0)<<" ";

        }
        cout<<endl;
    }
    }
}
