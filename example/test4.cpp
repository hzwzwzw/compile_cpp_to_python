#include <iostream>
#include <cctype>  // For isdigit and isspace
#include <cstdlib> // For atoi
#include <cstring> // For strlen

const int MAX = 100;

// Stack structure for characters (operators and parentheses)
class CharStack
{
public:
    char data[MAX];
    int top;
};

// Stack structure for integers (values)
struct IntStack
{
    int data[MAX];
    int top;
};

// Initialize character stack
void initCharStack(CharStack &stack)
{
    stack.top = -1;
}

// Initialize integer stack
void initIntStack(IntStack &stack)
{
    stack.top = -1;
}

// Push character onto stack
void pushChar(CharStack &stack, char c)
{
    if (stack.top < MAX - 1)
    {
        stack.data[++stack.top] = c;
    }
}

// Push integer onto stack
void pushInt(IntStack &stack, int value)
{
    if (stack.top < MAX - 1)
    {
        stack.data[++stack.top] = value;
    }
}

// Pop character from stack
char popChar(CharStack &stack)
{
    if (stack.top >= 0)
    {
        return stack.data[stack.top--];
    }
    return '\0'; // Return null character if stack is empty
}

// Pop integer from stack
int popInt(IntStack &stack)
{
    if (stack.top >= 0)
    {
        return stack.data[stack.top--];
    }
    return 0; // Return 0 if stack is empty
}

// Peek character stack
char peekChar(CharStack &stack)
{
    if (stack.top >= 0)
    {
        return stack.data[stack.top];
    }
    return '\0';
}

// Check if character is an operator
bool isOperator(char c)
{
    return c == '+' || c == '-' || c == '*' || c == '/';
}

// Get operator precedence
int precedence(char op)
{
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

// Convert infix expression to postfix using the Shunting Yard algorithm
void infixToPostfix(const char *infix, char *postfix)
{
    CharStack opStack;
    initCharStack(opStack);

    int j = 0;
    for (int i = 0; i < strlen(infix); ++i)
    {
        char token = infix[i];

        if (isspace(token))
        {
            continue;
        }

        if (isdigit(token))
        {
            // If the token is a number, add it to the output
            while (i < strlen(infix) && isdigit(infix[i]))
            {
                postfix[j++] = infix[i++];
            }
            postfix[j++] = ' '; // Separate numbers with space
            --i;
        }
        else if (token == '(')
        {
            // If the token is a left parenthesis, push it on the stack
            pushChar(opStack, token);
        }
        else if (token == ')')
        {
            // If the token is a right parenthesis, pop and output from the stack
            // until an left parenthesis is at the top of the stack
            while (opStack.top != -1 && peekChar(opStack) != '(')
            {
                postfix[j++] = popChar(opStack);
                postfix[j++] = ' ';
            }
            popChar(opStack); // Pop the left parenthesis
        }
        else if (isOperator(token))
        {
            // Operator
            while (opStack.top != -1 && precedence(peekChar(opStack)) >= precedence(token))
            {
                postfix[j++] = popChar(opStack);
                postfix[j++] = ' ';
            }
            pushChar(opStack, token);
        }
    }

    // Pop all the operators from the stack
    while (opStack.top != -1)
    {
        postfix[j++] = popChar(opStack);
        postfix[j++] = ' ';
    }
    postfix[j] = '\0';
}

// Evaluate postfix expression
int evaluatePostfix(const char *postfix)
{
    IntStack valStack;
    initIntStack(valStack);

    for (int i = 0; i < strlen(postfix); ++i)
    {
        char token = postfix[i];

        if (isspace(token))
        {
            continue;
        }

        if (isdigit(token))
        {
            int value = 0;
            while (i < strlen(postfix) && isdigit(postfix[i]))
            {
                value = value * 10 + (postfix[i] - '0');
                ++i;
            }
            pushInt(valStack, value);
            --i;
        }
        else if (isOperator(token))
        {
            int right = popInt(valStack);
            int left = popInt(valStack);
            switch (token)
            {
            case '+':
                pushInt(valStack, left + right);
                break;
            case '-':
                pushInt(valStack, left - right);
                break;
            case '*':
                pushInt(valStack, left * right);
                break;
            case '/':
                pushInt(valStack, left / right);
                break;
            }
        }
    }

    return popInt(valStack); // The final result is the last value in the stack
}

int main()
{
    const char expression[] = "1+(-5-22)*4/(2+1)";
    char postfix[MAX];

    infixToPostfix(expression, postfix);
    int result = evaluatePostfix(postfix);

    std::cout << "The result of the expression is: " << result << std::endl;

    return 0;
}
