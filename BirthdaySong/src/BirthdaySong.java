
public class BirthdaySong {
	String secondLine;
	String animal;
	String verb;
	
	BirthdaySong(String secondLine, String animal, String verb){
		this.secondLine = secondLine;
		this.animal = animal;
		this.verb = verb;
	}
	
	String getString(){
		String result = "Happy birthday to you,\nHappy birthday to you,\n";
		result = result + "You look like a " + this.animal + ",\n";
		result = result + "And you " + this.verb + " like one too.\n";
		return result;
	}
	
	public static void main(String[] args){
		BirthdaySong song = new BirthdaySong("you live in a zoo,", "tapir", "run");
		String songString = song.getString();
		System.out.println(songString);
	}
}
