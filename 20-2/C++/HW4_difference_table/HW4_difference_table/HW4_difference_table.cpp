#include<iostream>
using namespace std;
#define N 10

void datainput(int n,double arr[N][N]) //데이터 입력함수
{
	double x, y;
	for (int i = 0; i < n; i++) // x데이터 입력
	{
		cout << "Enter X" << i<<" : ";
		cin >> x;
		arr[0][i] = x;
	}
	for (int i = 0; i < n; i++) // y데이터 입력
	{
		cout << "Enter Y" << i << " : ";
		cin >> y;
		arr[1][i] = y;
	}
}

void diff(int n, double arr[N][N]) //차분계산 및 저장함수
{
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < n - 1; j++)
		{
			arr[i + 1][j] = arr[i][j + 1] - arr[i][j];
		}
	}
}

void divdiff(int n, double arr[N][N]) //분할차분계산 및 저장함수
{
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < n - 1; j++)
		{
			arr[i + 1][j] = (arr[i][j + 1] - arr[i][j]) / (arr[0][j + i] - arr[0][j]);
		}
	}
}

int main()
{
	int ndata;
	cout << "Number of data points? : ";
	cin >> ndata;
	double storage[N][N] = { 0 };
	datainput(ndata, storage);


	//입력된 X Y 데이터 출력
	cout << "Input X datas : ";
	for (int i = 0; i < ndata; i++)
	{
		cout << storage[0][i] << " ";
	}
	cout <<endl<< "Input Y datas : ";
	for (int i = 0; i < ndata; i++)
	{
		cout << storage[1][i] << " ";
	}
	cout << endl;


	//차분 계산 및 출력
	diff(ndata, storage);
	for (int i = 0; i < ndata - 1; i++)
	{
		cout << i + 1 << " order differences : ";
		for (int j = 0; j < ndata - (i + 1); j++)
		{
			cout << storage[i + 2][j] << " ";
		}
		cout << endl;
	}


	//분할차분 계산 및 출력
	divdiff(ndata, storage);
	for (int i = 0; i < ndata - 1; i++)
	{
		cout << i + 1 << " order divided differences : ";
		for (int j = 0; j < ndata - (i + 1); j++)
		{
			cout << storage[i + 2][j] << " ";
		}
		cout << endl;
	}
}
