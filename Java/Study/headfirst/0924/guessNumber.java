class Play{
	int number = 0;
	public void guess(){
		number = (int)(Math.random() * 10);
		System.out.println("The number is: " + number);
	}
}

class GuessPlayer{
	Play p1;
	Play p2;
	Play p3;
	public void startGame(){
			p1 = new Play();
			p2 = new Play();
			p3 = new Play();

			int p1GuessNum = 0;
			int p2GuessNum = 0;
			int p3GuessNum = 0;
			boolean p1IsTrue = false;
			boolean p2IsTrue = false;
			boolean p3IsTrue = false;
		while(true){
			int guessNum = (int)(Math.random()*10);
			p1.guess();
			p1GuessNum = p1.number;
			p2.guess();
			p2GuessNum = p2.number;
			p3.guess();
			p3GuessNum = p3.number;
			if(p1GuessNum == guessNum){
				p1IsTrue = true;
			}
			
			if(p2GuessNum == guessNum){
				p2IsTrue = true;
			}
			if(p3GuessNum == guessNum){
				p3IsTrue = true;
			}
			if(p1IsTrue || p2IsTrue || p3IsTrue){
				System.out.println("The guessNumber is: "+ guessNum);
				System.out.println("p1 player guess number is: " + p1GuessNum);
				System.out.println("p2 player guess number is: " + p2GuessNum);
				System.out.println("p3 player guess number is: " + p3GuessNum);
				break;
			} else {
				System.out.println("continue guess number is:  ");
			}
		}
	}
}

class GuessPlayerTestDriver{
	public static void main(String[] args){
		GuessPlayer man1 = new GuessPlayer();
		man1.startGame();
	}
}
