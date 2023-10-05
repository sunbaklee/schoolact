#include <iostream>
using namespace std;
#include <cmath>

typedef struct point {
	double x;
	double y;
}P;

double dist_2d(P first, P second) {
	return sqrt(pow((second.x - first.x), 2) + pow((second.y - first.y), 2));
}

void p9(){
	P first, second;
	cout <<" 첫번째 좌표를 입력해주세요: ";
	cin >> first.x >> first.y;
	cout <<" 두번째 좌표를 입력해주세요: ";
	cin >> second.x >> second.y;
	double dist;
	dist = dist_2d( first, second);
	cout <<"좌표("<< first.x <<","<< first.y <<"), ("<< second.x <<","<< second.y <<") "<<"사이의 거리는 "<< dist <<endl;
}

void quad_eqn(double a, double b, double c) {
	double check = pow(b, 2) - (4 * a * c);
	double ans =-b / (2 * a);
	if (check <0) {
		cout <<"해가 없습니다"<<endl;
		return;
	}
	else if (check ==0 ){
		cout <<"해는 "<< (-b + check) / (2 * a) <<"입니다."<<endl;
		return;
	}
	else {
		cout <<"해는 "<< (-b + check) / (2 * a) <<"와 "<< (-b - check) / (2 * a) <<"입니다."<<endl;
		return;
	}
}

void p10() {
	double a, b, c;
	cout <<"이차방정식의 계수를 입력해 주십시오"<<endl;
	cout <<"a: ";
	cin >> a;
	cout <<"b: ";
	cin >> b;
	cout <<"c: ";
	cin >> c;
	quad_eqn(a,b,c);
}

void main() {
	p9();
	p10();
}
