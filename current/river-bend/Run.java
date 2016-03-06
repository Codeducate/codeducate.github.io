class Puppy {
	int puppyAge;

	public Puppy(String name) { // constructor
		// This constructor has one parameter, name.
		System.out.println("Name chosen is: " + name);
	}

	public void setAge(int age) {
		puppyAge = age;
	}

	public int getAge() {
		System.out.println("Puppy's age is: " + puppyAge);
		return puppyAge;
	}
}

public class Run {
	public static void main(String[] args) {
		// Object creation
		Puppy myPuppy = new Puppy("Frodo");

		// Call class method to set puppy's age
		myPuppy.setAge(9);

		//Call another class method to get puppy's age
		int myPuppyAge = myPuppy.getAge();
	}
}
