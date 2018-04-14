class Dog{
	String name;
	void bark(){
		System.out.println(name + " say wangwang! ");
	}

	public static void main(String[] args){
		Dog d1 = new Dog();
		d1.name = "hashiqi";
		d1.bark();

		Dog [] myDog = new Dog[3];
		myDog[0] = new Dog();
		myDog[1] = new Dog();
		myDog[2] = d1;
		myDog[0].name = "erheizi";
		myDog[1].name = "huanghuang";
		int x = 0;
		while(x < myDog.length){
			myDog[x].bark();
			x++;
		}
	}
}
