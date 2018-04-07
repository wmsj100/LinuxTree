class dog3{
	String name;
	String getName(){
		return name;
	}

	void setName(String str){
		name = str;
	}
	public static void main(String[] args){
		dog3 one = new dog3();
		String str1 =	one.getName();
		System.out.println(str1);
		one.setName("wmsj100");
		str1 = one.getName();
		System.out.println(str1);
	}
}
