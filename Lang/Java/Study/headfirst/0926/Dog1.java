class Dog1{
	void bark(int count){
		while(count > 0){
			System.out.println("bark bark");
			count--;
		}
	}
	public static void main(String[] args){
		Dog1 one = new Dog1();
		one.bark(3);
	}
}
