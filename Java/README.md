# Java Basics Cheat Sheet ☕📚

## Part 1: Data Types & Variables

### What is a Variable?
A named storage location in memory that holds data of a specific type.

```java
String name = "Alice";  // Variable 'name' stores the text "Alice"
int age = 25;           // Variable 'age' stores the number 25
```

### Primitive Data Types

| Type | Size | Description | Example |
|------|------|-------------|---------|
| `byte` | 1 byte | Whole numbers from -128 to 127 | `byte b = 100;` |
| `short` | 2 bytes | Whole numbers from -32,768 to 32,767 | `short s = 10000;` |
| `int` | 4 bytes | Whole numbers from -2^31 to 2^31-1 | `int i = 100000;` |
| `long` | 8 bytes | Whole numbers from -2^63 to 2^63-1 | `long l = 100000L;` |
| `float` | 4 bytes | Fractional numbers (6-7 decimal digits) | `float f = 19.99f;` |
| `double` | 8 bytes | Fractional numbers (15 decimal digits) | `double d = 19.99;` |
| `char` | 2 bytes | Single character/letter | `char c = 'A';` |
| `boolean` | 1 bit | True or false values | `boolean flag = true;` |

### Reference Data Types
```java
String message = "Hello, World!";  // String object
int[] numbers = {1, 2, 3};         // Array
Object obj = new Object();          // Any class instance
```

**Static Typing**: Java requires explicit type declaration.

---

## Part 2: Operators in Java ⚙️

### Arithmetic Operators
```java
int a = 10, b = 3;
a + b;   // Addition → 13
a - b;   // Subtraction → 7
a * b;   // Multiplication → 30
a / b;   // Division → 3 (integer division)
a % b;   // Modulus (remainder) → 1
a++;     // Increment → 11
b--;     // Decrement → 2
```

### Comparison Operators (Return boolean)
```java
a == b;  // Equal to → false
a != b;  // Not equal to → true
a > b;   // Greater than → true
a < b;   // Less than → false
a >= b;  // Greater than or equal to → true
a <= b;  // Less than or equal to → false
```

### Logical Operators
```java
boolean x = true, y = false;
x && y;  // AND → false
x || y;  // OR → true
!x;      // NOT → false
```

### Assignment Operators
```java
int x = 5;    // Basic assignment
x += 3;       // Add and assign → x = x + 3 → 8
x -= 2;       // Subtract and assign → x = x - 2 → 6
x *= 2;       // Multiply and assign → x = x * 2 → 12
x /= 3;       // Divide and assign → x = x / 3 → 4
```

### Ternary Operator
```java
int result = (a > b) ? a : b;  // If a > b, result = a, else result = b
```

---

## Part 3: Control Flow 🔁

### Conditional Statements
```java
int age = 18;
if (age >= 18) {
    System.out.println("You are an adult");
} else if (age > 13) {
    System.out.println("You are a teenager");
} else {
    System.out.println("You are a child");
}

// Switch statement
int day = 3;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    default:
        System.out.println("Other day");
}
```

### Loops

**For Loop:**
```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);  // Prints 0 to 4
}

// Enhanced for loop (for-each)
int[] numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    System.out.println(num);
}
```

**While Loop:**
```java
int count = 0;
while (count < 5) {
    System.out.println(count);
    count++;
}

// Do-while loop
int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 5);
```

### Loop Control Statements
- `break`: Exit the loop completely
- `continue`: Skip to next iteration

```java
for (int i = 0; i < 5; i++) {
    if (i == 3) {
        break;  // Exit loop when i is 3
    }
    System.out.println(i);  // Prints 0, 1, 2
}
```

---

## Part 4: Methods 🧩

### Defining a Method
```java
// Method definition
public static void greet(String name) {
    System.out.println("Hello, " + name + "!");
}
```

### Calling a Method
```java
greet("Alice");  // Method call → "Hello, Alice!"
```

### Return Statement
```java
public static int add(int a, int b) {
    return a + b;  // Returns the sum
}

int result = add(3, 5);  // result = 8
```

### Method Overloading (Same name, different parameters)
```java
public static int add(int a, int b) {
    return a + b;
}

public static double add(double a, double b) {
    return a + b;
}
```

---

## Part 5: Arrays & Collections 📦

### Arrays
```java
// Declaration and initialization
int[] numbers = new int[5];           // Array of 5 integers
int[] numbers2 = {1, 2, 3, 4, 5};     // Array literal

// Accessing elements
numbers[0] = 10;                      // First element
int length = numbers.length;           // Array length

// Multi-dimensional array
int[][] matrix = {{1, 2, 3}, {4, 5, 6}};
```

### ArrayList (Dynamic array)
```java
import java.util.ArrayList;

ArrayList<String> fruits = new ArrayList<>();
fruits.add("Apple");      // Add element
fruits.add("Banana");
fruits.get(0);            // Get element → "Apple"
fruits.set(1, "Mango");   // Update element
fruits.remove(0);         // Remove element
fruits.size();            // Get size
```

### HashMap (Key-value pairs)
```java
import java.util.HashMap;

HashMap<String, Integer> ages = new HashMap<>();
ages.put("Alice", 25);    // Add key-value pair
ages.put("Bob", 30);
ages.get("Alice");        // Get value → 25
ages.containsKey("Bob");  // Check if key exists → true
ages.remove("Alice");     // Remove key
```

---

## Part 6: Classes & Objects 🧱

### Class Definition
```java
public class Car {
    // Fields (attributes)
    private String brand;
    private String model;
    
    // Constructor
    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }
    
    // Method
    public void drive() {
        System.out.println(brand + " " + model + " is driving");
    }
    
    // Getters and setters
    public String getBrand() {
        return brand;
    }
    
    public void setBrand(String brand) {
        this.brand = brand;
    }
}
```

### Creating Objects
```java
Car myCar = new Car("Toyota", "Camry");  // Create object
myCar.drive();                           // Call method → "Toyota Camry is driving"
System.out.println(myCar.getBrand());    // Access property → "Toyota"
```

### Inheritance
```java
public class Vehicle {  // Parent class
    public void start() {
        System.out.println("Vehicle starting");
    }
}

public class Car extends Vehicle {  // Child class
    @Override
    public void start() {
        System.out.println("Car starting");
        super.start();  // Call parent method
    }
}
```

### Encapsulation
```java
public class BankAccount {
    private double balance;  // Private field
    
    public double getBalance() {  // Public getter
        return balance;
    }
    
    public void deposit(double amount) {  // Public setter
        if (amount > 0) {
            balance += amount;
        }
    }
}
```

### Polymorphism
```java
// Method overriding
public class Animal {
    public void sound() {
        System.out.println("Animal makes sound");
    }
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

// Using polymorphism
Animal myAnimal = new Dog();
myAnimal.sound();  // Output: "Dog barks"
```

---

## Part 7: Exception Handling 🛡️

### Try-Catch Block
```java
try {
    int result = 10 / 0;  // This will throw ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero: " + e.getMessage());
} catch (Exception e) {
    System.out.println("General exception: " + e.getMessage());
} finally {
    System.out.println("This always executes");
}
```

### Throwing Exceptions
```java
public void checkAge(int age) throws Exception {
    if (age < 0) {
        throw new Exception("Age cannot be negative");
    }
}

// Using the method
try {
    checkAge(-5);
} catch (Exception e) {
    System.out.println(e.getMessage());
}
```

---

## Part 8: String Manipulation 🔤

### String Methods
```java
String text = "Hello, Java!";
text.length();              // Returns length → 12
text.toLowerCase();         // Converts to lowercase → "hello, java!"
text.toUpperCase();         // Converts to uppercase → "HELLO, JAVA!"
text.trim();                // Removes whitespace
text.replace("Java", "World");  // Replaces text → "Hello, World!"
text.substring(7);          // Gets substring from index → "Java!"
text.substring(0, 5);       // Gets substring from to → "Hello"
text.charAt(0);             // Gets character at index → 'H'
text.indexOf("Java");       // Finds index of substring → 7
text.contains("Java");      // Checks if contains → true
text.equals("Hello, Java!"); // Checks equality → true
text.split(", ");           // Splits into array → ["Hello", "Java!"]
```

### StringBuilder (Mutable strings)
```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");         // Add text
sb.append(" ");
sb.append("World");
String result = sb.toString();  // Convert to string → "Hello World"
sb.reverse();               // Reverse → "dlroW olleH"
```

---

## Part 9: Important Keywords 🧠

### Access Modifiers
- `public` - Accessible from any class
- `private` - Accessible only within its own class
- `protected` - Accessible within package and subclasses
- (default) - Accessible only within its package

### Other Important Keywords
- `static` - Belongs to the class rather than instances
- `final` - Cannot be changed (constant) or cannot be extended
- `void` - Method doesn't return a value
- `this` - Refers to the current object
- `super` - Refers to parent class
- `new` - Creates a new object
- `import` - Imports packages or classes
- `package` - Declares a package
- `instanceof` - Checks if object is instance of a class

---

## Part 10: Interfaces & Abstract Classes 📋

### Interface (Blueprint of a class)
```java
interface Animal {
    void sound();  // Abstract method (no body)
    void sleep();  // Abstract method
}

class Dog implements Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
    
    public void sleep() {
        System.out.println("Dog sleeps");
    }
}
```

### Abstract Class (Cannot be instantiated)
```java
abstract class Animal {
    // Abstract method (no implementation)
    public abstract void sound();
    
    // Regular method
    public void sleep() {
        System.out.println("Animal sleeps");
    }
}

class Dog extends Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

---

## Part 11: Java Standard Library 📚

### Common Utility Classes
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

// Arrays utility
int[] numbers = {3, 1, 4, 2, 5};
Arrays.sort(numbers);           // Sort array → [1, 2, 3, 4, 5]
int index = Arrays.binarySearch(numbers, 3);  // Binary search → 2

// Collections utility
ArrayList<Integer> list = new ArrayList<>(Arrays.asList(3, 1, 4, 2, 5));
Collections.sort(list);         // Sort list
Collections.reverse(list);      // Reverse list

// Random numbers
Random rand = new Random();
int randomNum = rand.nextInt(100);  // Random number between 0-99

// Date and time
import java.time.LocalDateTime;
LocalDateTime now = LocalDateTime.now();
System.out.println("Current time: " + now);
```

---

*Created By Shekher Saksham Shashi (AMPICS)*
