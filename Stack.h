
#include <iostream>
using namespace std;

//const int max = 100;

template <class Type>
class Stack {

private:
	Type arr[100];
	int top;
public:
	Stack() { top = -1; }
	void push(Type var);
	Type pop();
	bool isEmpty() {
		if (top == -1) return true;
		else return false;
	}
	bool isFull() {
		if (top == 100 - 1) return true;
		else return false;
	}
	Type peek() {
		try {
			if (top == 100 - 1 || top == -1) throw top;
			else return arr[top];
		}
		catch (int x) {
			cout << "Stack overflow!" << endl;
			exit(1);
		}
	}
};

template <class Type>
void Stack<Type> ::push(Type var) {

	try {
		if (top == 100 - 1) throw top;
		else
			arr[++top] = var;
	}

	catch (int x)
	{

		cout << "Stack overflow!" << endl;
		exit(1);
	}
}

template <class Type>

Type Stack<Type> :: pop() {

	try {
		if (top == -1) throw top;
		else return arr[top--];
	}
	catch (int x) {

		cout << "Stack underflow!" << endl;
		exit(1);
	}
}