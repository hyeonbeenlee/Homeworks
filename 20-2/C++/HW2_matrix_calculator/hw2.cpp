#include <iostream>
#define size 10 // size=10 입력으로 간편화 하는 것(단축키 개념). int size=10과는 다르다.
using namespace std;

void input(double matrix[size][size],int m,int n) // 행렬요소 입력용 함수
{
	cout << "A11 A12 A13....B11 B12 B13....형식으로 행렬 요소를 입력하세요." << endl;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> matrix[i][j];
		}
	}
}

void output(double matrix[size][size], int m, int n) // 행렬요소 출력용 함수
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << matrix[i][j] << " "; // 행 내에서 한 요소가 출력되면 공백으로 구분함
		}
		cout << endl; //한 행의 출력이 끝나면 줄바꿈 시행
	}
}

void sum(double matrix1[size][size], double matrix2[size][size],double matrix3[size][size],int m, int n) // 행렬 덧셈함수
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
			matrix3[i][j] = matrix1[i][j] + matrix2[i][j];
	}
}

void subtract(double matrix1[size][size], double matrix2[size][size], double matrix3[size][size], int m, int n) // 행렬 뺄셈함수
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
			matrix3[i][j] = matrix1[i][j] - matrix2[i][j];
	}
}

void product(double matrix1[size][size], double matrix2[size][size], double matrix3[size][size], int m, int n, int p, int q) //행렬 곱셈함수, 인수로 계산할 두 행렬, 결과행렬, 각 행렬의 크기를 받는다.
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < q; j++)
			for (int k = 0; k < p; k++)
			{
				matrix3[i][j] = matrix3[i][j] + matrix1[i][k] * matrix2[k][j]; // Cij=(Ai1*B1j)+(Ai2+B2j)+(Ai3*B3j).....공식을 이해한다.
			}
	}
}

int main()
{
	double A[size][size] = { 0 }; // 10*10 기저행렬 생성
	double B[size][size] = { 0 };
	double C[size][size] = { 0 }; // 결과 행렬 C
	int m, n, p, q; //행렬의 크기 변수
	char calc,repeat; // 연산자 입력용
	
	do
	{
		cout << "첫 번째 행렬을 입력하세요." << endl << "행의 수는? (최대 10) : ";
		cin >> m;
		cout << "열의 수는? (최대 10) : ";
		cin >> n;
		input(A, m, n); // 받은 m, n과 10*10 영행렬 기반으로 입력 시행
		cout << "입력받은 행렬은" << endl;
		output(A, m, n); // 입력받은 내용물을 보여줌

		cout << "두 번째 행렬을 입력하세요." << endl << "행의 수는? : ";
		cin >> p;
		cout << "열의 수는? : ";
		cin >> q;
		input(B, p, q);
		cout << "입력받은 행렬은" << endl;
		output(B, p, q);

		cout << "계산할 연산자를 입력해주세요(+, -, *) : ";
		cin >> calc;

		switch (calc)
		{
		case '+':
			if (m == p && n == q)
			{
				cout << "연산 결과는" << endl;
				sum(A, B, C, m, n);
				output(C, m, n);
				break;
			}
			else
			{
				cout << "차원이 맞지 않습니다" << endl;
				break;
			}

		case '-':
		{
			if (m == p && n == q)
			{
				cout << "연산 결과는" << endl;
				subtract(A, B, C, m, n);
				output(C, m, n);
				break;
			}
			else
			{
				cout << "차원이 맞지 않습니다" << endl;
				break;
			}
		}

		case '*':
		{
			if (n == p)
			{
				cout << "연산 결과는" << endl;
				product(A, B, C, m, n, p, q);
				output(C, m, q);
				break;
			}
			else
			{
				cout << "차원이 맞지 않습니다" << endl;
				break;
			}
		}

		default:
		{
			cout << "올바른 연산자를 입력해주세요." << endl;
			break;
		}

		}
		cout << "다시 하려면 Y를 눌러주세요. 다른 키 입력 시 종료합니다. : ";
		cin >> repeat;
	} while (repeat == 'y' || 'Y');
	return 0;
}

