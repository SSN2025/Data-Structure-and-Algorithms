#include <iostream>
#include<complex>
#include <bits/stdc++.h>
#include<cmath>


using namespace std;
int two_pow(int n){
   int p =1;
   while(p<n)p *=2;
   return p;
   
}
void insert0s (vector<double>&v,int n){
    vector<double>x(n - v.size(),0);
    v.insert(v.end(),x.begin(),x.end());
}

vector<complex<double>> fft(vector<double>A){
    int n = A.size();
    if(n==1)return {complex<double>(A[0],0)};
    vector<double>Aeven,Aodd;
    for(int i=0;i<n;i+=2)Aeven.push_back(A[i]);
    for(int i=1;i<n;i+=2)Aodd.push_back(A[i]);

    vector<complex<double>>Yeven,Yodd,Y(n);
    Yeven = fft(Aeven);
    Yodd = fft(Aodd);

    complex<double>w,t;
    for(int i =0;i<= n/2-1;i++){
        double q = (-2*M_PI*i )/n;
        w = exp(complex<double>(0,q));
        t = w * Yodd[i];
        Y[i]       = Yeven[i] + t;
        Y[i + n/2] = Yeven[i] - t;
    }
    return Y;
}

vector<complex<double>> ifft(vector<complex<double>>A){
    int n = A.size();
    if(n==1)return A;
    vector<complex<double>>Aeven,Aodd;
    for(int i=0;i<n;i+=2)Aeven.push_back(A[i]);
    for(int i=1;i<n;i+=2)Aodd.push_back(A[i]);

    vector<complex<double>>Yeven,Yodd,Y(n);
    Yeven = ifft(Aeven);
    Yodd = ifft(Aodd);

    complex<double>w,t;
    for(int i =0;i<= n/2-1;i++){
        double q = (2*M_PI*i )/n;
        w = exp(complex<double>(0,q));
        t = w * Yodd[i];
        Y[i]       = Yeven[i] + t;
        Y[i + n/2] = Yeven[i] - t;
    }
    return Y;
}




vector<double> multiply(vector<double>&poly1,vector<double>&poly2){
        int n1 = poly1.size();
        int n2 = poly2.size();
        int n = n1+n2-1;
        n = two_pow(n);
        insert0s(poly1,n);
        insert0s(poly2,n);

        vector<complex<double>>a_ ,b_,c_;
        a_ = fft(poly1);
        b_ = fft(poly2);

        for(int i=0;i<n;i++){
            c_.push_back(a_[i] * b_[i]);
        }
    //Inverse fft:
    c_ = ifft(c_);
    vector<double>C(n,0);
    for(int i = 0;i<n;i++)C[i] = round(c_[i].real()/n);
    while(C.back()==0)C.pop_back();
return C;
}

int main() {
    vector<double> a,b;
    a = {1,2,4,1};
    b= {3,2,1};
    vector<double> ans = multiply(a,b);
    cout<<"Multiplied Polynomial: ";
    for(double i : ans){
        cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}