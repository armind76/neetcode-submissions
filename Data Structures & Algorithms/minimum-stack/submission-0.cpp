class MinStack {
public:
    stack<int> mainStack;
    stack<int> minStack;
    MinStack() {
        
    }
    
    void push(int val) {
        mainStack.push(val);
        minStack.push(std::min(val, minStack.empty() ? val:minStack.top()));

    }
    
    void pop() {
        mainStack.pop();
        minStack.pop();
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
