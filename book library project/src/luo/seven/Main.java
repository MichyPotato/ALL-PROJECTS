/* Michelle Luo
 * AP CSA
 * Period 7
 * FGE: Library 3000
 */

package luo.seven; 

//Line 78 - Imports
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URLEncoder;
import java.util.Scanner;
import java.net.URL;
import java.net.URI;
import java.net.URISyntaxException;

public class Main { 

    //Line 90 - Main method
    public static void main(String args[]) throws Exception { 
        ArrayList<Cipher> library= new ArrayList<Cipher>(); 
        BufferedReader readCSV = new BufferedReader(new FileReader("src/luo/seven/books.csv")); 
        String line = "";
        String[] fields = new String[6];
        while(line != null) {
            try { 

                //Reads fields from the CSV file and stores in the arrayList Library
                line = readCSV.readLine();
                fields = line.split(",");
                library.add(new Cipher(fields[0], fields[1], fields[2], Integer.parseInt(fields[3] ), 
                Float.parseFloat(fields[4]), Boolean.parseBoolean(fields[5])));
            } catch(Exception e) { 

                //Catch exceptions
                continue;
            }
        }
        readCSV.close(); 

        //Line 106 - Asks for user input on what book they want
        System.out.print("\033[H\033[2J");
        System.out.println("Choose a captivating book:");
        for(Cipher book : library) {
            System.out.println("  - \033[1;31m" + book.getName() + "\u001B[0m by " + book.getAuthor());
        }
        System.out.print("Your choice: ");
        Cipher chosenBook = null;
        Scanner selectionScanner = new Scanner(System.in); 
        
        //Line 114 - Do-While loop to receive and evaluate user input
        do { 
            String selection = selectionScanner.nextLine().toLowerCase();
            for(Cipher book : library) { 

                //Check if user input is a valid book that is in the library
                if(selection.equalsIgnoreCase(book.getName())){
                    System.out.println("You have chosen " + book.getName() + " -- " + book);
                    chosenBook = book;
                }
            }
        } while(chosenBook == null);

        
        //Line 123 - Do-While loop to run multiple algorithms with the book
        Boolean exit = false; 
        do { 

            //Line 125 - Option selection menu to receive user input
            System.out.println("Would you like to:" 
                                + "\n\033[1;31mA\u001B[0m) Read the book"
                                + "\n\033[1;31mB\u001B[0m) Encrypt a message"
                                + "\n\033[1;31mC\u001B[0m) Translate the book into Spanish"
                                + "\n\033[1;31mD\u001B[0m) Exit"); 

            //Line 130 - Evaluate user input with a switch statement
            String chosenAction = selectionScanner.nextLine();
            BufferedReader readBook = new BufferedReader(new FileReader(chosenBook.getTextFilePath())); 

            switch (chosenAction.toLowerCase()) { 

                //Line 133 - Case 'a' prints out the entire book based on the text file
                case "a": 

                    //For each line in the book, read the line
                    for(int i = 0; i < chosenBook.getNumberOfLines(); i++) {
                        line = readBook.readLine(); 

                        //Ternary Operator: if the line is null, print out a empty line. Else, print out line
                        System.out.println((line == null) ? ("") : (line));
                    }
                    break; 

                //Line 139 - Case 'b' encodes a message using the modified book cipher invented by Michelle Luo
                case "b":
                    System.out.print("You wish to use the book to encode a message. Enter the message: ");
                    String[] message = selectionScanner.nextLine().toLowerCase().split(" "); 
                    
                    //Split the 'secret message' into its word components
                    String encryptedMessage = "";
                    for(int i = 0; i < message.length; i++) { 
                        
                        //Line 144 - Use the wordFinder function (listed below the main) to encrypt
                        encryptedMessage += wordFinder(message[i], chosenBook);
                    }
                    System.out.println(encryptedMessage);
                    break; 

                
                //Line 148 - Case 'c' translates a book using Google Translate API
                case "c": 

                    //For each line in the book, read the line
                    for(int i = 0; i < chosenBook.getNumberOfLines(); i++) {
                        line = readBook.readLine(); 
                        
                        //Ternary Operator: if the line is null, print out a empty line.
                        //Else, print out a translated line. 
                        System.out.println( (line == null) ? ("") : (translate("en", "es", line)) );
                    }
                    break; 

                //Line 154 - Case 'd' allows the user to exit the program
                case "d":
                    exit = true;
                    break; 

                //Line 157 - Default Case will remind user that only A, B, C, & D are accepted
                default:
                    System.out.println("Enter in A B C or D. \n");
                    break;
            }
        } while(exit == false);
        selectionScanner.close();
    } 


    //Line 164 - This function's parameters are a plain text word and a cipher book
    //It returns an encrypted number
    static String wordFinder (String word, Cipher chosenBook) throws Exception { 
        
        //Line 165 - The word 'the' is given an unrelated set value to throw off cipher breakers
        if("the".equalsIgnoreCase(word)){return Float.toString(chosenBook.getCipherCodeForThe()) + " ";}
        BufferedReader readBook = new BufferedReader(new FileReader(chosenBook.getTextFilePath())); 
        
        //Line 167 - Search through every line of the book
        for(int i = 0; i < chosenBook.getNumberOfLines(); i++) {
            String line = readBook.readLine();
            try { 
                
                //Split the line into words that are stored in the Array wordsInLine
                String[] wordsInLine = line.split(" "); 
                
                //Search through wordsInLine
                for(int j = 0; j < wordsInLine.length; j++) {
                    if(wordsInLine[j].equalsIgnoreCase(word)){ 
                        
                        //If the current word of wordsInLine matches the plain text word, then:
                        readBook.close();
                        if(chosenBook.isReversed()){ 
                            
                            //If the cipher is set on Reversed mode, 
                            //Then return numbers for if the text file was being read backwards
                            return (chosenBook.getNumberOfLines() - i - 1) 
                            + "." + (wordsInLine.length - j) + " "; 
                        } else { 
                            
                            //If not Reversed, return a number with the format line#.word#
                            return (i + 1) + "." + (j + 1) + " ";
                        }
                    }
                }
            } catch(Exception e) { 
                
                //Handle exceptions like null lines
                continue;
            }
        }
        readBook.close(); 
        
        //If no match is found in the book, return the plaintext word
        return word + " ";
    } 

    
    //Line 200 - Translate method is a edited version of the code found here: 
    //https://stackoverflow.com/questions/8147284/how-to-use-google-translate-api-in-my-java-application
    private static String translate(String langFrom, String langTo, String text)
        throws IOException, URISyntaxException { 
        
        //Generate link
        String urlStr = "https://script.google.com/macros/s/AKfycbwJHnDAQTgTivvCSk3dEi3Xoj3d4-" + 
                "eLD7q9at6wRwMFnKtPDnybK4gN9nSWO1JMpnn3/exec" +
                "?q=" + URLEncoder.encode(text, "UTF-8") +
                "&target=" + langTo +
                "&source=" + langFrom; 
        
        //Create a URL object
        URL url = new URI(urlStr).toURL();
        StringBuilder response = new StringBuilder(); 
        
        //Establish HTTP connection on the URL
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestProperty("User-Agent", "Mozilla/5.0");
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine; 
        
        //Read the input
        while((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close(); 
        
        //Return the translated string
        return response.toString();
    }
}
//Final Line Count: 221