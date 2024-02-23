/* Michelle Luo
 * Cmdr. Schenk
 * October 19th
 * AP CSA
 * Main Class
 */


/* Michelle Luo’s EXTRA STUFF THAT SHE DID
 * CSV File- load 13 fields into each coordinate in the 2D array
 * REGEX parsing for commands (look at the USE case for best example)
 * Zork-like Game Mechanism where it tells the player what paths next to the current coordinate ate available to go to.
 * Complex Death- Coordinates (loaded thru the CSV) that may contain a higher Chance of Death, and a randomizer selects whether you will die based on that Chance... Useful for further Game Engine development :D if given a bit of extra time, would tweak a bit to make it simpler though.
 */


//Imports 
package luo.seven;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher; 
import java.util.Random;
import java.io.BufferedReader;
import java.io.FileReader;

//Main Method
public class Main{
    public static void main(String args[])throws Exception{
        
        //clear screen
        System.out.print("\033[H\033[2J");
        System.out.flush();
        //Variables initialization
        int index = 0;
        int xPos = 11;
        int yPos = 2;
        int potentialYPos = 0;
        int potentialXpos = 0;
        int pastXPos = 11;
        int pastYPos = 2;
        boolean gatekeep = false;
        boolean gameLoop = true;
        int winCondition = 0;
        Random rand = new Random();
        //ArrayList and Array initialization
        Coordsys[][] coordsysArray = new Coordsys[25][25];
        BufferedReader reader = new BufferedReader(new FileReader("src/luo/seven/coordsys.csv"));
        String line = reader.readLine();
        String[] fields = line.split(",");
        coordsysArray[Integer.parseInt(fields[0])][Integer.parseInt(fields[1])] = new Coordsys(Integer.parseInt(fields[0]), Integer.parseInt(fields[1]), Boolean.parseBoolean(fields[2]), Boolean.parseBoolean(fields[3]), Boolean.parseBoolean(fields[4]), Boolean.parseBoolean(fields[5]), fields[6], Integer.parseInt(fields[7]), Integer.parseInt(fields[8]), Integer.parseInt(fields[9]), fields[10], fields[11], Boolean.parseBoolean(fields[12]));
        while( line != null) {
            // read the next line
            try {
                 line = reader.readLine();
                fields = line.split(",");
                coordsysArray[Integer.parseInt(fields[0])][Integer.parseInt(fields[1])] = new Coordsys(Integer.parseInt(fields[0]), Integer.parseInt(fields[1]), Boolean.parseBoolean(fields[2]), Boolean.parseBoolean(fields[3]), Boolean.parseBoolean(fields[4]), Boolean.parseBoolean(fields[5]), fields[6], Integer.parseInt(fields[7]), Integer.parseInt(fields[8]), Integer.parseInt(fields[9]), fields[10], fields[11], Boolean.parseBoolean(fields[12]));
            } catch (Exception e) {
                continue;
            }
        }
        reader.close();
        //create arraylists for inventory and items
        ArrayList<Item> inventory = new ArrayList<Item>();
        ArrayList<Item> allItems = new ArrayList<Item>();
        //ITEM CALL
        Item nullItem = new Item(0);
        Item mints = new Item(1, "MINTS", "There is a pack of MINTS littered on the ground.", OnInventory.heldByCharacter, 0);
        Item painting = new Item(2, "PAINTING", "A classical PAINTING lies forlornly on the ground.", OnInventory.onGround, 0);
        Item sword = new Item(3, "SWORD", "An anmagical SWORD is stuck in the ground.", OnInventory.onGround, 0);
        Item sack = new Item(4, "SACK", "A lone SACK lies on the ground.", OnInventory.onGround, 0);
        Item armor = new Item(5, "ARMOR", "ARMOR lies on the road, forgotten.", OnInventory.onGround, 0);
        Item key = new Item(6, "KEY", "A KEY lies curiously on the ground", OnInventory.onGround, 0);
        Item gold = new Item(7, "GOLD", "A heavy chunk of GOLD is on the ground.", OnInventory.onGround, 0);
        Item flippers = new Item(8, "FLIPPERS", "swimming FLIPPERS on the ground!!!!", OnInventory.onGround, 0);
        Item token = new Item(9, "TOKEN", "An engraved TOKEN on the ground!!!!", OnInventory.onGround, 0);
        Item bucket = new Item(10, "BUCKET", "A BUCKET sits right there... very lonely.", OnInventory.onGround, 0);
        Item runes = new Item(11, "RUNES", "Some Old RUNES are scattered on the ground", OnInventory.onGround, 0);
        Item coin1 = new Item(12, "COIN", "A momentous treasure of a single COIN is on the ground", OnInventory.onGround, 0);
        Item coin2 = new Item(13, "COIN", "A momentous treasure of a single COIN is on the ground", OnInventory.onGround, 0);
        Item coin3 = new Item(14, "COIN", "A momentous treasure of a single COIN is on the ground", OnInventory.onGround, 0);
        Item torch = new Item(15, "TORCH", "a TORCH is implanted in the ground...", OnInventory.heldByCharacter, 0);    
        //add items to the list of all items
        allItems.add(nullItem);
        allItems.add(mints);
        allItems.add(painting);
        allItems.add(sword);
        allItems.add(sack);
        allItems.add(armor);
        allItems.add(key);
        allItems.add(gold);
        allItems.add(flippers);
        allItems.add(token);
        allItems.add(bucket);
        allItems.add(runes);
        allItems.add(coin1);
        allItems.add(coin2);
        allItems.add(coin3);
        //Character Call
        Character nullCharacter = new Character();
        Character statue = new Character(1, "IMPOSING STATUE", "There is an IMPOSING STATUE looking down at you...", 11, false, false, "The UNIMPOSING STATUE has a spot for a RUNE on its chest...", "The UNIMPOSING STATUE is alive! It whispers to you: You need to use some MINTS to cool down the Dragon breath... or else face my fate of stone...");
        Character dragonKing = new Character(2, "DRAGONKING", "A DRAGONKING looks down at you...", 1, false, false, "it opens its mouth... to eat your face or breathe fire?", "The DRAGONKING smiles amicably at you... and lets you pass on as you please.");
        Character artCollector = new Character(3, "ART COLLECTOR", "An ART COLLECTOR stands in front of the road to beyond.", 2, false, true, "The ART COLLECTOR demands a payment from you... but it seems he only accepts art...", "The ART COLLECTOR smiles and lets you pass...");
        Character nowhere = new Character(4, "NOWHERE the GOD", "NOWHERE the GOD stands in stasis in front of you...", 4, false, false, "NOWHERE opens his eyes into your soul... and demands payment and sacrifices if you ever wish to leave this world...", "NOWHERE asks you: would you like to ascend this world?");
        Character ferryman = new Character(5, "FERRYMAN", "A FERRYMAN stands on his boat waiting for clients to take across the river...", 9, false, false,  "He requires a TOKEN from you if you wish to cross to the Beyond...", "The FERRYMAN brought you to your DEMISE!!!!! MWAHAHAHHAHAHA");
        Character rabbit = new Character(6, "RABID RABBIT", "A RABID RABBIT stands before you with a cutting glare...", 3, false, false, "It wants a sword from you...", "The RABID RABBIT then smiles at you and wishes you a good day... thank goodness it didn't decide to use the sword on you...");
        Character muttrUker = new Character(7, "muttrUker", "a dragon named MUTTRUKER stands before you...", 1, false, false, "it opens its mouth.. and whew! its breath is STINKY STINKY STINKY", "MUTTRUKER smiles at you and you no longer smell his bad breath!");
        Character python = new Character(8, "PYTHON", "a large poisonous PYTHON stares back at you with beady eyes...", 10, false,false, "It looks like it wants a home... a BUCKET perhaps?", "PYTHON is happy!");
        Character vendingMachine = new Character(9, "VENDING MACHINE", "a large VENDING MACHINE stands right there...", 12, false, false,"A note is written on it that says: payment accepted by COIN", "The VENDING MACHINE broke down...");
        Character deathTroll = new Character(10, "DEATH TROLL", "A DEATH TROLL stands before you with a menacing smirk and a raised club...", 0, false,false, "It smashes it on your head!", "DEATH TROLL lies on the floor, knocked out... because there is no death in this supposedly nonviolent game...");
        Character oracle = new Character(11, "ORACLE", "A withered ORACLE stands on a stool in front of you, breathing her nasty breath on you...", 1, false, false, "She probably needs either MINTS or a COVID19 Face mask...", "The oracle smiles at you with her nice breath and tells you: NOWHERE the GOD requires ARMOR and GOLD in order for you to ascend out of this forsaken world...");
        Character student = new Character(12, "ASLEEP STUDENT", "An ASLEEP STUDENT lies on the floor of this cave... ", 0, false, false, "he's not waking up either...", "he woke up!");
        Character bucketTroll = new Character(13, "BUCKET TROLL", "A BUCKET TROLL stands before you... ", 10, false, true, "maybe it wants something related to buckets?", "The Bucket Troll was defeated... with cute adorable lil snakey fellas that slithered out to distract him! The Bucket Troll disappeared off into the distance grinning...");
        //Add Characters to list of allCharacters
        ArrayList<Character> allCharacters = new ArrayList<Character>();
        allCharacters.add(nullCharacter);
        allCharacters.add(statue);
        allCharacters.add(dragonKing);
        allCharacters.add(artCollector);
        allCharacters.add(nowhere);
        allCharacters.add(ferryman);
        allCharacters.add(rabbit);
        allCharacters.add(muttrUker);
        allCharacters.add(python);
        allCharacters.add(vendingMachine);
        allCharacters.add(deathTroll);
        allCharacters.add(oracle);
        allCharacters.add(student);
        allCharacters.add(bucketTroll);
        //Initial prompt
        String promptForCoord = "You are standing in front of the edge of a cliff, along the East-West Cliff Edge Path.";
        Scanner userInputScanner = new Scanner(System.in);
        Pattern pattern;
        Matcher matcher;
        String userInputParsing[];
        String userInput;
        // do while loop for user input
        do{
            //Print out the coordinate prompt
            System.out.println("\033[1;31m" + promptForCoord + "\u001B[0m");
            //Print out things in the Vicinity of the Coordinate: other locations, characters, and items...
            printThingsInVicinity(xPos, yPos, coordsysArray, allItems, allCharacters);
            //If there is some character blocking the way, set gatekeep to true
            if ((allCharacters.get(coordsysArray[xPos][yPos].getCharacterId()).isDefeated() == false) && (allCharacters.get(coordsysArray[xPos][yPos].getCharacterId()).isGateKeeper() == true)){
                gatekeep = true;
            }else{
                gatekeep = false;
            }
            // Use ONLY for game developer cheats
            // System.out.println("(" + xPos + ", " + yPos + ")");
            //user INPUT scanner
            System.out.print("\033[1;33m" + ">>> " + "\u001B[0m");
            //split the input up by spaces to parse individually
            userInput = userInputScanner.nextLine().toLowerCase();
            userInputParsing = userInput.split(" ");
            System.out.print("\033[1;33m");
            //Switch statements to parse userInput[0], or the first word in the User Input from earlier.
            switch (userInputParsing[0]) {
                //If user wants to go North:
                case "north":
                case "n":
                    potentialYPos = yPos + 1;
                    //if there is a character blocking the way:
                    if ((gatekeep == true) && (potentialYPos != pastYPos)){
                        System.out.println("Can't go there!");
                    }
                    //check if the space is within bounds and accessible
                    else if (((potentialYPos <= 24) && (coordsysArray[xPos][potentialYPos].isAccessibleFromSouth() == true))){
                        pastYPos = yPos;
                        yPos += 1;
                    }
                    else{
                        System.out.println("Can't go there!!!!! Why do you bump into walls so much anyways... its almost like this is a only-text adventure game...");
                    }
                    break;
                //If user wants to go South:
                case "south":
                case "s":
                    potentialYPos = yPos - 1;
                    //if there is a character blocking the way:
                    if ((gatekeep == true) && (potentialYPos != pastYPos)){
                        System.out.println("Can't go there!");
                    }
                    //check if the space is within bounds and accessible
                    else if (((potentialYPos >= 0) && (coordsysArray[xPos][potentialYPos].isAccessibleFromNorth() == true))){
                        pastYPos = yPos;
                        yPos -= 1;
                    }
                    else{
                        System.out.println("Can't go there!!!!! Why do you bump into walls so much anyways... its almost like this is a only-text adventure game...");
                    }
                    break;
                //If user wants to go East:
                case "east":
                case "e":
                    potentialXpos = xPos + 1;
                    //if there is a character blocking the way:
                    if ((gatekeep == true) && (potentialXpos != pastXPos)){
                        System.out.println("Can't go there!");
                    }
                    //check if the space is within bounds and accessible
                    else if (((potentialXpos <= 24) && (coordsysArray[potentialXpos][yPos].isAccessibleFromWest() == true))){
                        pastXPos = xPos;
                        xPos += 1;
                    }
                    else{
                        System.out.println("Can't go there!!!!! Why do you bump into walls so much anyways... its almost like this is a only-text adventure game...");
                    }
                    break;
                //If user wants to go West
                case "west":
                case "w":
                    potentialXpos = xPos - 1;
                    //if there is a character blocking the way:
                    if ((gatekeep == true) && (potentialXpos != pastXPos)){
                        System.out.println("Can't go there!");
                    }
                    //check if the space is within bounds and accessible
                    else if (((potentialXpos >= 0) && (coordsysArray[potentialXpos][yPos].isAccessibleFromEast() == true)) || ((gatekeep == true) && (potentialXpos == pastXPos))){
                        pastXPos = xPos;
                        xPos -= 1;
                    }
                    else{
                        System.out.println("Can't go there!!!!! Why do you bump into walls so much anyways... its almost like this is a only-text adventure game...");
                    }
                    break;
                //take the item
                case "t":
                case "take":
                case "pickup":
                case "pick":
                case "grab":
                    //retrieve the itemId of the alleged item on that coordinate
                    index = coordsysArray[xPos][yPos].getItemId();
                    //if the item exists, and there is space for the item, then pick it up
                    if ((index != 0) && (inventory.size() < 8)){
                        //special exception for sack, because it has a unique functionality
                        if (index == 7){
                            if (inventory.contains(sack)) {
                                sack.setThingsContainedWithin(sack.getThingsContainedWithin() + 1);
                            } else {
                                System.out.println("no SACK to pick up the gold with...");
                            }
                        }
                        else{
                        inventory.add(allItems.get(index));
                        System.out.println("Picked up " + allItems.get(index).getItemName() + ".");
                        coordsysArray[xPos][yPos].setItemId(0);
                        }
                    //if no space in the backpack...
                    }else if (inventory.size() >= 8){
                        System.out.println("Inventory is too full to hold more...");
                    // if there is no item at the coordinate aka item id = 0...
                    }else{
                        System.out.println("no items here....");
                    }
                    break;
                //drop the item
                case "d":
                case "drop":
                    //try catch block to catch instances when the user does not use a second word
                    try {
                        //set regex pattern and matcher to try and find which item user wants to drop
                        pattern = Pattern.compile("(mints)|(painting)|(sword)|(sack)|(armor)|(key)|(gold)|(flippers)|(token)|(bucket)|(runes)|(coin)|(coin)|(coin)|(torch)", Pattern.CASE_INSENSITIVE);
                        matcher = pattern.matcher(userInputParsing[1]);
                        matcher.find();
                        boolean containsItem = false;
                        boolean haventMatchedYet = true;
                        //cycle through each pattern, and each item in inventory to determine if the item can be dropped or not
                        for (int i = 0; (i < 15) && (haventMatchedYet==true); i++) {
                            if (userInputParsing[1].equalsIgnoreCase(matcher.group(i))){
                                for (Item item : allItems) {
                                    if (item.getItemName().equals(matcher.group(i).toUpperCase())){
                                        containsItem = true;
                                        if (coordsysArray[xPos][yPos].getItemId() != 0){
                                            System.out.println("Can't drop! Theres already an item there....");
                                        }
                                        else{
                                        inventory.remove(item);
                                        coordsysArray[xPos][yPos].setItemId(item.getItemId());
                                        System.out.println("Dropped " + item.getItemName() + ".");
                                        haventMatchedYet = false;
                                        }
                                    }
                                }
                                if (containsItem == false){
                                    System.out.println("You can't drop something you don't have....");
                                }
                            } else {
                                System.out.println("drop what? drop it like its hot????? please type it again with more specificity....");
                            }
                        }
                    } catch (Exception e) {
                        System.out.println("drop what? drop it like its hot????? please type it again with more specificity....");
                    }
                    break;
                //if the user wants to use an item
                case "u":
                case "use":
                    //try catch block to catch instances when the user does not use a second word
                    try {
                        //switch statement using lower case version of it
                        switch (userInputParsing[1].toLowerCase()) {
                            //use mints:
                            case "mints":
                                if (inventory.contains(mints) == false){
                                    System.out.println("You can't use something you don't have....");
                                }
                                else{
                                    if ((coordsysArray[xPos][yPos].getCharacterId() == 2) || (coordsysArray[xPos][yPos].getCharacterId() == 7) || (coordsysArray[xPos][yPos].getCharacterId() == 11)){
                                        inventory.remove(mints);
                                        System.out.println("Your mints were confiscated by " + allCharacters.get(coordsysArray[xPos][yPos].getCharacterId()).getCharacterName() + " to alleviate the effects of bad breath...");
                                        allCharacters.get(coordsysArray[xPos][yPos].getCharacterId()).setDefeated(true);
                                    } else {
                                        inventory.remove(mints);
                                        System.out.println("your breath now smells marginally better.... i wonder what else you could have used these for...");
                                    }
                                }
                                break;
                            //user painting
                            case "painting":
                                if (inventory.contains(painting) == false){
                                    System.out.println("You can't use something you don't have....");
                                }
                                else{
                                    if (coordsysArray[xPos][yPos].getCharacterId() == 3){
                                        inventory.remove(painting);
                                        artCollector.setDefeated(true);
                                        System.out.println("The art collector took your painting as payment for further passage.");
                                    } else {
                                        System.out.println("Can you really use the painting here??? In the middle of nowhere??? You must be crazy...");
                                    }
                                }
                                break;
                            //use sword, not in the traditional way ofc
                            case "sword":
                                if (inventory.contains(sword) == false){
                                    System.out.println("You can't use something you don't have....");
                                }
                                else{
                                    if (coordsysArray[xPos][yPos].getCharacterId() != 0){
                                        if (coordsysArray[xPos][yPos].getCharacterId() == 6){
                                            inventory.remove(sword);
                                            inventory.add(torch);
                                            rabbit.setDefeated(true);
                                            System.out.println("The RABID RABBIT gave you a TORCH in exchange for the SWORD..."); 
                                                //rabid rabbit
                                        }else{
                                        System.out.println("you tried to attack... but it failed, thanks to your horrible sword skills");
                                        }
                                    } else {
                                        System.out.println("Can't use the sword in this game! Supposedly this game features non-violence...");
                                    }
                                }
                                break;
                            // use sack
                            case "sack":
                                if (inventory.contains(sack) == false){
                                    System.out.println("You can't use something you don't have....");
                                }
                                else{
                                    if (coordsysArray[xPos][yPos].getItemId() == 7){
                                        coordsysArray[xPos][yPos].setItemId(0);
                                        sack.setItemName("SACK");
                                        sack.setThingsContainedWithin(sack.getThingsContainedWithin() + 1);
                                        System.out.println("You pick up the gold, filling up your SACK. It now contains some gold inside.");
                                    }
                                    else{
                                    System.out.println("You try to use the sack by opening up the sack and wishing there were presents in there from Santa, but you've been too naughty this year... ");
                                    }
                                }
                                break;
                            // use armor
                            case "armor":
                                if (inventory.contains(armor) == false){
                                        System.out.println("You can't use something you don't have....");
                                    }
                                else{
                                    if (coordsysArray[xPos][yPos].getCharacterId() == 4){
                                        inventory.remove(armor);
                                        System.out.println("NOWHERE the GOD took your armor as payment for screwing up your life...");
                                        winCondition += 1;
                                    } else {
                                        System.out.println("use armor??? but theres nothing to protect yourself from...");
                                    }
                                }
                                break;
                            // use key
                            case "key":
                                if (inventory.contains(key) != true){
                                        System.out.println("You can't use something you don't have....");
                                    }
                                else{
                                    if ((xPos == 3) && (yPos == 5)) {
                                        inventory.remove(key);
                                        System.out.println("The key opened the door... but now its stuck there...");
                                        coordsysArray[xPos+1][yPos].setAccessibleFromWest(true);;
                                        coordsysArray[xPos][yPos].setAccessibleFromEast(true);;
                                    } else {
                                        System.out.println("Now, I wonder what do you use a key on... is it not obvious???? A locked door perhaps???");
                                    }
                                }
                                break;
                            // use gold
                            case "gold":
                                if (sack.getThingsContainedWithin() == 0){
                                        System.out.println("You can't use something you don't have....");
                                    }
                                else
                                    if (coordsysArray[xPos][yPos].getCharacterId() == 4){
                                        sack.setThingsContainedWithin(0);
                                        System.out.println("NOWHERE the GOD took your gold as payment for screwing up your life... your sack no longer contains gold inside...");
                                        winCondition += 1;
                                    } else {
                                        System.out.println("u cannot use the gold here... u can only give it up as payment...");
                                    }                            
                                break;
                            // use flippers
                            case "flippers":
                                if (inventory.contains(flippers) == false){
                                        System.out.println("You can't use something you don't have....");
                                }
                                else if (coordsysArray[xPos][yPos].getGeneralLocation() == "THE LAKE"){
                                    System.out.println("u tried swimming, but the lake is too disgusting for you to sink your godly body into...");
                                }
                                else{
                                    System.out.println("cannot use flippers in a non-watery or non-calm environment...");
                                }
                                break;
                            // use token
                            case "token":
                                if (inventory.contains(token) == false){
                                        System.out.println("You can't use something you don't have....");
                                    }
                                else if (coordsysArray[xPos][yPos].getCharacterId() == 5){
                                    System.out.println("THE FERRYMAN IS TAKING YOU TO THE UNDERWORLD! FEAR YOUR IMMENENT DEMISE.");
                                    gameLoop = false;
                                } else {
                                    System.out.println("You look at the token and it has a picture of a boat on it... you probably can't use it here in the middle of nowhere then...");
                                }
                                break;
                            // use bucket
                            case "bucket":
                                if (inventory.contains(bucket) == false){
                                        System.out.println("You can't use something you don't have....");
                                    }
                                else if ((coordsysArray[xPos][yPos].getCharacterId() == 8)){
                                    coordsysArray[xPos][yPos].setCharacterId(0);
                                    bucket.setThingsContainedWithin(bucket.getThingsContainedWithin() + 1);
                                    System.out.println("Picked up a PYTHON with the BUCKET! Seems like the lil fella slithered in...");
                                }else if ((coordsysArray[xPos][yPos].getCharacterId() == 13)){
                                    coordsysArray[xPos][yPos].setCharacterId(0);
                                    bucket.setThingsContainedWithin(bucket.getThingsContainedWithin() - 1);
                                    bucketTroll.setDefeated(true);
                                    System.out.println("The Bucket Troll was defeated... with cute adorable lil snakey fellas that slithered out to distract him! The Bucket Troll disappeared off into the distance grinning...");
                                }else{
                                    System.out.println("you can't use the snake BUCKET here...");
                                }
                                break;
                            // use runes
                            case "runes":
                                if (inventory.contains(runes) == false){
                                        System.out.println("You can't use something you don't have....");
                                }
                                else if (coordsysArray[xPos][yPos].getCharacterId() == 1){
                                    statue.setDefeated(true);
                                    System.out.println("the statue awoke!");
                                }
                                else{
                                    System.out.println("you can't use the RUNES here... maybe use it on an unimposing statue....?");
                                }
                                break;
                            // use coin
                            case "coin":
                                if ((inventory.contains(coin1) == false) && (inventory.contains(coin2) == false) && (inventory.contains(coin3) == false)){
                                        System.out.println("You can't use something you don't have....");
                                    }
                                else if (coordsysArray[xPos][yPos].getCharacterId() == 9){
                                    if (inventory.contains(coin1)){
                                        inventory.remove(coin1);
                                    }
                                    else{
                                        if (inventory.contains(coin2)){
                                            inventory.remove(coin2);
                                        }
                                        else{
                                            inventory.remove(coin3);
                                        }
                                    }
                                    System.out.println("inserted a coin! got a mint back in return...");
                                    inventory.add(mints);
                                }else{
                                    System.out.println("Cannot use coins here... it seems as if they aren't accepted as currency here...");
                                }
                                break;
                            default:
                                System.out.println(".... did you spell the item right???? its supposed to be: use itemWithCorrectSpellingHere.... do better next time...");
                                break;
                        }
                    } catch (Exception e) {
                        System.out.println("Use what???? are you using me in this relationship????? you are a mean player and I would never date you...");
                    }
                    
                    break;
                // help for user
                case "h":
                case "help":
                    System.out.println("Enter N, S, E, W to go in different directions. \nI for inventory \nEG for exiting the game \nT for picking up an item \nD <item name here> for dropping an item.\nU <item name here> to use an item. \nItems limited to one per square. \nEnjoy!");
                    break;
                // look for user
                case "l":
                case "look":
                case "see":
                case "view":
                    //if there is anything accessible in a certain direction, it prints out instructions for it.
                    if ((coordsysArray[xPos][yPos + 1].isAccessibleFromSouth() == true)){
                        System.out.print(coordsysArray[xPos][yPos + 1].getUserLookPrompt() + " to the north.");
                    }if ((coordsysArray[xPos][yPos - 1].isAccessibleFromNorth() == true)){
                        System.out.print(coordsysArray[xPos][yPos - 1].getUserLookPrompt() + " to the south.");
                    }if ((coordsysArray[xPos + 1][yPos].isAccessibleFromWest() == true)){
                        System.out.print(coordsysArray[xPos + 1][yPos].getUserLookPrompt() + " to the east.");
                    }if ((coordsysArray[xPos -1][yPos].isAccessibleFromEast() == true)){
                        System.out.print(coordsysArray[xPos - 1][yPos].getUserLookPrompt() + " to the west.");
                    }
                    System.out.println();
                    break;
                // inventory
                case "i":
                case "inventory":
                case "backpack":
                case "storage":
                    index = 1;
                    for (Item item : inventory) {
                        System.out.println(index + ". " + item.getItemName());
                        index += 1;
                    }
                    break;
                //exit game
                case "exit game":
                case "eg":
                    gameLoop = false;
                    break;
                // CHEAT CODES
                case "1234":
                    inventory.add(coin1);
                    inventory.add(coin2);
                    inventory.add(coin3);
                    xPos = 23;
                    yPos = 5;
                    System.out.println("Gave player all 3 COINS and teleported to (23, 5), or the Hall of the Oracle in the Ancient Cult Corridor");
                    break;
                // CHEAT CODES
                case "2345":
                    bucket.setThingsContainedWithin(4);
                    inventory.add(bucket);
                    xPos = 18;
                    yPos = 23;
                    System.out.println("Gave Player BUCKET with 4 pythons inside and Teleported to the Bucket Trolls (18,23)");
                    break;
                // CHEAT CODES
                case "3456":
                    inventory.add(painting);
                    xPos = 4;
                    yPos = 10;
                    System.out.println("Gave Player PAINTING and Teleported to the Art Collector (4,10)");
                    break;
                // CHEAT CODES
                case "4567":
                    sack.setThingsContainedWithin(1);
                    inventory.add(armor);
                    inventory.add(sack);
                    xPos = 1;
                    yPos = 21;
                    System.out.println("Gave Player GOLD and Teleported to the Road to Nowhere (1, 21)");
                    break;
                //Snark the user outta here if they misspell something...
                default:
                    System.out.println("I cannot tell with your snarky attitude. Please try again...");
                    break;
            }
            //death algorithm, to check whether there is a probability of death, execute someone if they happen to fall into it...
            promptForCoord = "\n" + coordsysArray[xPos][yPos].getGeneralLocation();
            if (coordsysArray[xPos][yPos].getChanceOfDeath() != 0){
                if (rand.nextInt(coordsysArray[xPos][yPos].getChanceOfDeath()) != 0){
                    System.out.println(coordsysArray[xPos][yPos].getDeathString());
                    gameLoop = false;
                }
            }
            System.out.print("\u001B[0m");
            if (winCondition == 2){
                System.out.println("\033[1;31mWith NOWHERE's demand's satisfied... you ascended out of this world... YOU WIN!\u001B[0m");
                gameLoop = false;
            }
        //while for while the game is still running and there is no death
        }while(gameLoop == true);
        //close scanner to prevent memory leaks
        userInputScanner.close();

    }
    
    public static void printThingsInVicinity(int xPos, int yPos, Coordsys[][] coordsysArray, ArrayList<Item> allItems, ArrayList<Character> allCharacters ){
        //If there are places to go in any direction that are different from the current location, print out the prompt for them
        if ((coordsysArray[xPos][yPos + 1].isAccessibleFromSouth() == true) && (coordsysArray[xPos][yPos + 1].getGeneralLocation().equalsIgnoreCase(coordsysArray[xPos][yPos].getGeneralLocation()) == false)){
            System.out.print(coordsysArray[xPos][yPos + 1].getUserLookPrompt() + " to the \033[1;34mnorth\u001B[0m.");
        }if ((coordsysArray[xPos][yPos - 1].isAccessibleFromNorth() == true) && (coordsysArray[xPos][yPos - 1].getGeneralLocation().equalsIgnoreCase(coordsysArray[xPos][yPos].getGeneralLocation()) == false)){
            System.out.print(coordsysArray[xPos][yPos - 1].getUserLookPrompt() + " to the \033[1;34msouth\u001B[0m.");
        }if ((coordsysArray[xPos + 1][yPos].isAccessibleFromWest() == true)&& (coordsysArray[xPos + 1][yPos].getGeneralLocation().equalsIgnoreCase(coordsysArray[xPos][yPos].getGeneralLocation()) == false)){
            System.out.print(coordsysArray[xPos + 1][yPos].getUserLookPrompt() + " to the \033[1;34meast\u001B[0m.");
        }if ((coordsysArray[xPos -1][yPos].isAccessibleFromEast() == true) && (coordsysArray[xPos - 1][yPos].getGeneralLocation().equalsIgnoreCase(coordsysArray[xPos][yPos].getGeneralLocation()) == false)){
            System.out.print(coordsysArray[xPos - 1][yPos].getUserLookPrompt() + " to the \033[1;34mwest\u001B[0m.");
        }
        System.out.println();
        //get the item id for the coordinate
        int index = coordsysArray[xPos][yPos].getItemId();
        // Print out an item prompt if the item exists at that coordinate
        if (index != 0){
            System.out.println(allItems.get(index).getItemOnGroundPrompt());
        }
        index = coordsysArray[xPos][yPos].getCharacterId();
        if (index != 0){
            System.out.print(allCharacters.get(index).getCharacterPrompt());
            if (allCharacters.get(index).isDefeated() == true){
                System.out.println(allCharacters.get(index).getDefeatedPrompt());
            }else {
                System.out.println(allCharacters.get(index).getUndefeatedPrompt());
            }
        }
    }

}