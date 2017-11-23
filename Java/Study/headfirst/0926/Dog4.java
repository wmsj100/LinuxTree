class Dog4{
	private int size;
	public int getter(){
		return size;
	}
	public void setter(int num){
		size = num;
	}
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

class Dog4TestDriver{
	public static void main(String[] args){
		Dog4 one = new Dog4();
		one.setter(80);
		Dog4 two = new Dog4();
		two.setter(20);
		Dog4 three = new Dog4();
		three.setter(8);
		one.bark();
		two.bark();
		three.bark();
	}
}
