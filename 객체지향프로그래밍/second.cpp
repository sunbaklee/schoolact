#include <iostream >
#include <algorithm >
using namespace std;
double calc_Avg(double a[], int tc) {
	double sum =0;
	double avg;
	for (int i =0; i < tc; i ++) {
		sum += a[i];
	}
	avg = sum / tc;
	return avg;
}
double calc_Dev(double a[], int tc) {
	double sum =0;
	double avg = calc_Avg(a, tc);
	for (int i =0; i < tc; i ++) {
		sum += (a[i] - avg) * (a[i] - avg);
	}
	sum /= tc;
	return sum;
}
void P3() {
	double a[10];
	int tc;
	cout <<"몇개를 입력하실 예정인지 여쭈어봐도 되겠습니까? :";
	cin >> tc;
	for (int i =0; i < tc; i ++){
		cin >> a[i]; 
	}
	cout << calc_Avg(a, tc) <<" "<< calc_Dev(a, tc) <<endl;
}
void sum_Row(int arr[][5], int * row) {
	int sum =0;
	for (int i =0; i <3; i ++) {
		for (int j =0; j <5; j ++) {
			sum += arr[i][j];
		}
		row[i] = sum;
		sum =0;
	}
}
void sum_Col(int arr[][5], int * col) {
	int sum =0;
	for (int i =0; i <5; i ++) {
		for (int j =0; j <3; j ++) {
			sum += arr[j][i];
		}
		col[i] = sum;
		sum =0;
	}
}
void P5() {
	int arr[3][5] = { 12,56,32,16,98,
					  99,56,34,41,3,
					  65,3,87,78,21 };
	int row[3];
	int col[5];
	sum_Row(arr, row);
	sum_Col(arr, col);
	for (int i =0; i <3; i ++) {
		cout << row[i] <<endl;
	}
	cout <<endl;
	for (int j =0; j <5; j ++) {
		cout << col[j] <<endl;
	}
}
void copy(int * A, int * B, int n) {
	for (int i =0; i < n; i ++) {
		B[i] = A[i];
	}
	for (int i =0; i < n; i ++) {
		cout << B[i] <<endl;
	}
}
void P9() {
	int A[100];
	int B[100];
	int n;
	cout <<"배열의 길이를 알려주십시오 :";
	cin >> n;
	cout <<"배열 A 입력";
	for (int i =0; i < n; i ++) {
		cin >> A[i];
	}
	copy(A, B, n);
}
void get_stat(double * A, double * p_avg, double * p_max, double * p_sum) {
	int tc =0;
	for (int i =0; A[i] !=NULL; i ++) {
		tc++;
	}
	sort(A, A + tc, greater <double >());
	*p_max = A[0];
	double sum =0;
	for (int i =0; i < tc; i ++){
		sum += A[i];
	}
	*p_sum = sum;
	*p_avg = sum / tc;
}
void P11() {
	double A[100];
	int tc;
	cout <<"입력받을 배열의 개수 : ";
	cin >> tc;
	for (int i =0; i < tc; i ++) {
		cin >> A[i];
	}
	A[tc] =NULL;
	double p_avg, p_max, p_sum;
	get_stat(A, &p_avg, &p_max, &p_sum);
	cout <<"평균: "<< p_avg <<endl <<"최댓값"<< p_max <<endl <<"합"<< p_sum <<endl;
}
void main() {
	P3();
	P5();
	P9();
	P11();
}