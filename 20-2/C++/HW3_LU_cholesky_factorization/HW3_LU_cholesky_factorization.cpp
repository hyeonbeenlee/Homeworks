#include <iostream>
#include <cmath>								//sqrt(x),pow(x,n) 함수 사용 위해 도입
#define N 10									//사용될 배열은 모두 N*N 크기로 통일한다.
using namespace std;



void Input(double mat[N][N],int n)				
												//인수로 입력된 10*10 배열mat에서 (0:n-1, 0:n-1) 주소의 요소를 입력받는다.
{
	int i, j;
	cout << "요소를 입력하세요.(A11 A12...A21 A22...)" << endl;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			cin >> mat[i][j];
		}
	}
}



void Output(double mat[N][N],int n) 			
												//인수로 입력된 10*10 배열mat에서 (0:n-1, 0:n-1) 주소의 요소를 출력한다.
{
	int i,j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			cout << mat[i][j] << " ";
		}
		cout << endl;							//한 행의 출력이 끝나면 줄바꿈
	}
	cout << endl;
}



double Transpose(double mat1[N][N],double mat2[N][N], int n)
												//인수로 입력된 10*10배열 mat2의 (0:n-1, 0:n-1) 주소에 10*10배열 mat1 의 요소들을 전치시켜 저장한 뒤, 10*10배열 mat2를 반환한다.
{
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			mat2[i][j] = mat1[j][i];
		}
	}
	return mat2[N][N];
}



void Factorize(double mat[N][N], int n)
												//인수로 입력된 10*10배열 mat으로부터 n차원의 Cholesky decomposition을 계산하여 출력한다
{
	double L[N][N] = { 0 };						//영배열로 초기화
	int i, j, k;
	for (i = 0; i < n; i++)						//모든 행에 대하여 루프
	{
		for (j = 0; j < i+1; j++)				// i+1? i가 0부터 시작하므로, i+1을 넣어줘야 루프가 돌아진다.					
		{										//i+1이 아니라 i로 넣어주면, i=0일 때 j=0;j<0 이므로 j++ 실행불가, j=0에서 루프 중단됨

			double sum = 0;						//시그마 항을 저장할 변수

			if (i == j)							//대각선 요소에 대해 먼저 계산
			{
				for (k = 0; k < j-1; k++)		//시그마 루프, j-1회 돌린다. 공식과 동일하게 적용
				{
					sum += pow(L[j][k], 2);		//대각선 요소 공식에서 시그마 기호 안의 식
				}
				L[j][j] = sqrt(mat[j][j] - sum);
			}
			else
			{
				for (k = 0; k < j-1; k++)		//시그마 루프, j-1회 돌린다. 공식과 동일하게 적용
				{
					sum += L[i][k] * L[j][k];	//Off-diagonal 요소 공식에서 시그마 기호 안의 식
				}
				L[i][j] = (mat[i][j] - sum) / L[j][j];
												//공식 그대로 적용
			}
		}
	}
	double U[N][N] = { 0 };
	Transpose(L, U, n);							//U에 L의 전치행렬을 저장한 뒤 반환

	cout << "계산된 L은" << endl;
	Output(L, n);								//L 출력
	cout << "계산된 U(LT)는" << endl;
	Output(U, n);								//U 출력
}



int main()										//메인함수
{
	double A[N][N] = { 0 };
	int n;

	cout << "정방행렬 차원은 : ";
	cin >> n;
	Input(A, n);								//A의 행렬요소 입력받는다

	cout << endl << "입력받은 행렬은" << endl;
	Output(A, n);								//A의 행렬요소 출력한다

	Factorize(A, n);							//A의 Cholesky Decomposition을 출력한다
		
	return 0;
}