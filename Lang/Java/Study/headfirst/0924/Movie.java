class Movie{
	String name;
	String genre;
	int rating;
	void playIt(){
		System.out.println("playing the movie...");
	}
}

class MovieTestDeriver{
	public static void main(String[] args){
		Movie one = new Movie();
		one.name = "movei sky";
		one.genre="blue";
		one.rating = 12;
		one.playIt();
	}
}
