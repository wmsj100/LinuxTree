public class simpleDotComTestDrive {
	public static void main(String[] args){
		simpleDotCom dot = new simpleDotCom();
		int[] locations = {2,3,4};
		dot.setLocationCells(locations);
		String userGuess = "2";
		String result = dot.checkYourself(userGuess);
		userGuess = "3";
		result = dot.checkYourself(userGuess);
		userGuess = "32";
		result = dot.checkYourself(userGuess);
		userGuess = "4";
		result = dot.checkYourself(userGuess);
	}
}
