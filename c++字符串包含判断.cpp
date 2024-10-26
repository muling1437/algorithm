#include <bits/stdc++.h>
using namespace std;
int n;
string a, b;

bool isContain(string str1, string str2)
{

    if (str1.find(str2) != string::npos)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    cin>>a>>b;
    cout << isContain(a, b);
}