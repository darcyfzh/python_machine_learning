#include <stack>
class Queue
{
public:
	Queue();
	~Queue();
	void addToTail(int node);
	int delHead();
private:
	stack<int> stack1;
	stack<int> stack2;
};

void Queue::addToTail(int a)
{
	stack1.push(a);
}

int delHead()
{
	if(stack2.size() <= 0)
	{
		while(stack1.size() > 0)
		{
			int value = stack1.top();
			stack1.pop();
			stack2.push(value);
		}
	}
	int head = stack2.top();
	stack2.pop();
	return head
}