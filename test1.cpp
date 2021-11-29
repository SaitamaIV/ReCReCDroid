#include<iostream>
using namespace std;
int main(){
	int a,b,c,d;
	cin >> a >> b;
	a *= 2;
	b = ++a * 3;
	c = (a + b - 1) / 2;
	d = b--;
	cout << a << " " << b << " " << c << " " << d << endl;
	return 0;
}
