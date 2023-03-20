# 150. Evaluate Reverse Polish Notation

## Content

* You are given an array of strings tokens that represents an arithmetic expression in a **Reverse Polish notation**.
* Evaluate the expression. Return an integer that represents the value of the expression.

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```



## What is Reverse Polish notation?

* It is a method for conveying mathematical expression without using parentheses (). 
* The operation is read from left to right but execution is done every time an operator is reached.
* Advantages: Faster and using less space to do calculation as parentheses are not needed in the formula.
* Use **stack** to solve these problem



## Example

* 5 1 - 3 * 
* --> (5 - 1) * 3 = 12

1. Push 5 into the stack. --> First Number
2. Push 1 into the stack. --> Second Number
3. Apply the subtraction operation by taking two operands from the stack (1 and 5). The first number (5) is subtracted from second number, and the result (4) is stored back to the stack. It is the only value in the stack.
4. Push 3 into the stack.
5. Apply the multiplication by taking two operands from the stack (4 and 3) and multiply them. The result (12) is then placed back into the stack. 
6. As the stack now only contains the number 12, return 12 as the answer.



## Approach 1: Using stack

* Loop through the whole expression.
  1. If it is number/operand, push it to the stack
  2. If it is operator, then pop up two number, calculate the result, and push back the result to stack.
* PsuedoCode are shown at the following.

```
stack = new Stack()
for each token in tokens:
	if token is a number:
		stack.push(token)
	else token is operator (+-*/):
		number_2 = stack.pop()
		number_1 = stack.pop()
		result = apply_operator(token, number_1, number_2)
		stack.push(result)
return stack.pop()
```



## Approach 1: Code

* Acutal Code for the question

```java
class Solution150 {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (String token : tokens) {
            // push number(operand) into the stack
            // if operator (+-*/), pop two numbers, calculate
           if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
               int secondNum = (int) stack.pop();
               int firstNum = (int) stack.pop();
               if (token.equals("+")) {
                   stack.push(firstNum + secondNum);
               } else if (token.equals("-")) {
                   stack.push(firstNum - secondNum);
               } else if (token.equals("*")) {
                   stack.push(firstNum * secondNum);
               } else if (token.equals("/")) {
                   stack.push(firstNum / secondNum);
               }
           } else {
               stack.push(Integer.valueOf(token));
           }
        }
        return (int) stack.pop();
    }
}
```

* Time Complexity: O(n), where n is the length of the array.
  * We need to do the linear search, and process all operators.
  * Therefore, the total cost is proportional to the length of the input array.
* Space complexity: O(n) / O(n/2)
  * In the worst case, the stack will have all the numbers on it at the same time. This is never more than half the length of the input array.
