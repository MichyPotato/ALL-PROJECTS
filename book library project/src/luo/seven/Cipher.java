/* Michelle Luo
 * AP CSA
 * Period 7
 * FGE: Library 3000
 */

/* Features of this program:
 * Multiple books in the Library (can add more by editing the CSV)
 * Integrated Google Translate API set up for translations to Spanish
 * Michelle's modified Book Cipher (adapted for TXT files) in JAVA
 * Being able to read the entire book in the Terminal
 */

package luo.seven;
public class Cipher { 

    //Line 3 - Variables/fields declaration
    private String name;
    private String author;
    private String textFilePath;
    private int numberOfLines;
    private float cipherCodeForThe;
    private boolean isReversed; 

    //Line 9 - Constructors in the order of default, partial, and full
    public Cipher() {
        this.name = "untitled";
        this.author = "anonymous";
        this.textFilePath = "";
        this.numberOfLines = 0;
        this.cipherCodeForThe = 0;
        this.isReversed = false;
    }
    public Cipher(String textFilePath, int numberOfLines, float cipherCodeForThe, boolean isReversed) {
        this.name = "untitled";
        this.author = "anonymous";
        this.textFilePath = textFilePath;
        this.numberOfLines = numberOfLines;
        this.cipherCodeForThe = cipherCodeForThe;
        this.isReversed = isReversed;
    }
    public Cipher(String name, String author, String textFilePath, int numberOfLines, float cipherCodeForThe,
            boolean isReversed) {
        this.name = name;
        this.author = author;
        this.textFilePath = textFilePath;
        this.numberOfLines = numberOfLines;
        this.cipherCodeForThe = cipherCodeForThe;
        this.isReversed = isReversed;
    } 

    //Line 33 - Getters and setters
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getAuthor() {
        return author;
    }
    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTextFilePath() {
        return textFilePath;
    }
    public void setTextFilePath(String textFilePath) {
        this.textFilePath = textFilePath;
    }
    public int getNumberOfLines() {
        return numberOfLines;
    }
    public void setNumberOfLines(int numberOfLines) {
        this.numberOfLines = numberOfLines;
    }
    public float getCipherCodeForThe() {
        return cipherCodeForThe;
    }
    public void setCipherCodeForThe(float cipherCodeForThe) {
        this.cipherCodeForThe = cipherCodeForThe;
    }
    public boolean isReversed() {
        return isReversed;
    }
    public void setReversed(boolean isReversed) {
        this.isReversed = isReversed;
    } 

    //Line 70 - The toString override
    public String toString(){
        return this.name + " is a book by " + this.author + "."
        + "\nYou can find this book at " + this.textFilePath + " and it has " + this.numberOfLines + " lines."
        + " The cipher has the keyword THE as " + this.cipherCodeForThe 
        + " and it is " + ((this.isReversed == true)?"":"not ") + "reversed.";
    }
} 

//75 lines total