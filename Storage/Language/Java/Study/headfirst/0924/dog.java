class Dog{
	int size;
	String breed;
	String name;
	void bark(){
		System.out.println("bark bark wanwang");
	}
}

class dogTestDriver{
	public static void main(String[] args){
		Dog d = new Dog();
		d.size = 13;
		d.bark();
	}
}
