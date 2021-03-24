#include<bits/stdc++.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <cstdlib>

using namespace std;


int main()
{
    int n,m,a,b;
    cin>>n>>m>>a>>b;
    int ar[n+1];
    for(int i=1;i<=n;i++)
    {
        ar[i]=1001;
    }
    ar[0]=0;
   /* cout<<"a= "<<a<<endl;
    cout<<"n= "<<n<<endl;
    cout<<"m= "<<m<<endl;
    cout<<"b= "<<b<<endl;
    cout<<endl;
    */
    for(int i=1;i<=n;i++)
    {

      /*  cout<<"i= "<<i<<endl;
        cout<<"ar[i-m]+b= "<<ar[i-m]+b<<endl;
        cout<<"i*a= "<<i*a<<endl;
        */
        if((i-m)>=0)
            ar[i]=min(ar[i-m]+b,i*a);
        else
            ar[i]=i*a;

    }

    for(int i=0;i<=n;i++)
    {
        cout<<ar[i]<<" ";
    }

    cout<<ar[n]<<endl;
}

