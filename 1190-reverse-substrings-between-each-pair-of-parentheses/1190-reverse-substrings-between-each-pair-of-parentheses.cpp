class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> openParenthese;
        string result;
        for (char curChar:s){
            if(curChar == '(' ){
                openParenthese.push(result.length());   // store the current length as the start index for later and reversal

            } else if(curChar == ')' ){
                int start = openParenthese.top();
                openParenthese.pop();
                reverse(result.begin() + start, result.end());    // reverse the substring between the mathching parentheses

            } else {
                result += curChar;     // append non-parenthesis characters to the processed string

            }
        }
        
        return result;
        
    }
};