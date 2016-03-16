public class Math
{
	public static int add(int number1, int number2)
	{
		return number1 + number2;
	}

	public static int subtract(int number1, int number2){
		return number1 - number2;
	}

	public static void greet(String name){

		System.out.println("Hello " + name);

	}

	public static void greaterThanTen(int number){

		if(number > 10) {
			System.out.println("Number is greater than ten");
		}
		else {
			System.out.println("Number is less than or equal to ten");
		}

	}

	public static void main(String args[])
	{
		int sum;
		int difference;
		sum = add(1, 2);
		System.out.println("Sum is " + sum);
		difference = subtract(1, 2);
		System.out.println("Difference is " + difference);
		greet("Allen");
		greaterThanTen(100000);
	}
}