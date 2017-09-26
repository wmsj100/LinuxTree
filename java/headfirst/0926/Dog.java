class Dog{
	int size;
	void bark(){
		if(size > 60){
			System.out.println("bark bark");
		} else if(size > 14){
			System.out.println("bik bik");
		} else {
			System.out.println("pi pi");
		}
	} 
}

class DogTestDriver{
	public static void main(String[] args){
		Dog one = new Dog();
		one.size = 80;
		Dog two = new Dog();
		two.size = 20;
		Dog three = new Dog();
		three.size = 8;
		one.bark();
		two.bark();
		three.bark();
	}
}
