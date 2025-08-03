#include <iostream>
#include <cmath>

using namespace std;

// Simple function to calculate square root using Newton-Raphson method
double calculateSqrt(double number) {
    if (number < 0) {
        cout << "Error: Cannot find square root of negative number!" << endl;
        return -1;
    }
    
    if (number == 0 || number == 1) {
        return number;
    }
    
    double x = number / 2.0; // Initial guess
    double prev_x;
    double precision = 0.000001;
    
    do {
        prev_x = x;
        x = (prev_x + number / prev_x) / 2.0;
    } while (abs(x - prev_x) > precision);
    
    return x;
}

int main() {
    double number;
    
    cout << "Enter a number to find its square root: ";
    cin >> number;
    
    double result = calculateSqrt(number);
    
    if (result != -1) {
        cout << "Square root of " << number << " is: " << result << endl;
        
        // Using built-in function for comparison
        cout << "Built-in sqrt() result: " << sqrt(number) << endl;
    }
    
    return 0;
}