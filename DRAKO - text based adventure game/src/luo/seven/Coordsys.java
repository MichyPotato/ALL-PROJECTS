/* Michelle Luo
 * Cmdr. Schenk
 * October 19th
 * AP CSA
 * Coordsys (Coordinate System) POCO Class 
 */

package luo.seven;

public class Coordsys {
    // initialize Coordsys fields
    private int xPos;
    private int yPos;
    private boolean accessibleFromNorth;
    private boolean accessibleFromSouth;
    private boolean accessibleFromWest;
    private boolean accessibleFromEast;
    private String generalLocation;
    private int itemId;
    private int characterId;
    private int chanceOfDeath;
    private String deathString;
    private String userLookPrompt;
    private boolean accessibility;
    //Constructor Default
    public Coordsys(){
        this.xPos = 0;
        this.yPos = 0;
        this.accessibleFromNorth = false;
        this.accessibleFromSouth = false;
        this.accessibleFromWest = false;
        this.accessibleFromEast = false;
        this.generalLocation = "";
        this.itemId = 0;
        this.characterId = 0;
        this.chanceOfDeath = 0;
        this.deathString = "";
        this.userLookPrompt = "";
        this.accessibility = false;
    }
    //Constructor Partial
    public Coordsys(int itemId){
        this.xPos = 0;
        this.yPos = 0;
        this.accessibleFromNorth = false;
        this.accessibleFromSouth = false;
        this.accessibleFromWest = false;
        this.accessibleFromEast = false;
        this.generalLocation = "";
        this.itemId = itemId;
        this.characterId = 0;
        this.chanceOfDeath = 0;
        this.deathString = "";
        this.userLookPrompt = "";
        this.accessibility = false;
    }
    //Constructor Partial
    public Coordsys(String generalLocation, int itemId, int characterId, String userLookPrompt){
        this.xPos = 0;
        this.yPos = 0;
        this.accessibleFromNorth = false;
        this.accessibleFromSouth = false;
        this.accessibleFromWest = false;
        this.accessibleFromEast = false;
        this.generalLocation = generalLocation;
        this.itemId = itemId;
        this.characterId = characterId;
        this.chanceOfDeath = 0;
        this.deathString = "";
        this.userLookPrompt = userLookPrompt;
        this.accessibility = false;
    }
    //Constructor Full
    public Coordsys(int xPos, int yPos, boolean accessibleFromNorth, boolean accessibleFromSouth, boolean accessibleFromWest, boolean accessibleFromEast, String generalLocation, int itemId, int characterId, int chanceOfDeath, String deathString, String userLookPrompt, boolean accessibility){
        this.xPos = xPos;
        this.yPos = yPos;
        this.accessibleFromNorth = accessibleFromNorth;
        this.accessibleFromSouth = accessibleFromSouth;
        this.accessibleFromWest = accessibleFromWest;
        this.accessibleFromEast = accessibleFromEast;
        this.generalLocation = generalLocation;
        this.itemId = itemId;
        this.characterId = characterId;
        this.chanceOfDeath = chanceOfDeath;
        this.deathString = deathString;
        this.userLookPrompt = userLookPrompt;
        this.accessibility = accessibility;
    }
    // Getters and Setters
    public int getxPos() {
        return xPos;
    }
    public void setxPos(int xPos) {
        this.xPos = xPos;
    }
    public int getyPos() {
        return yPos;
    }
    public void setyPos(int yPos) {
        this.yPos = yPos;
    }
    public boolean isAccessibleFromNorth() {
        return accessibleFromNorth;
    }
    public void setAccessibleFromNorth(boolean accessibleFromNorth) {
        this.accessibleFromNorth = accessibleFromNorth;
    }
    public boolean isAccessibleFromSouth() {
        return accessibleFromSouth;
    }
    public void setAccessibleFromSouth(boolean accessibleFromSouth) {
        this.accessibleFromSouth = accessibleFromSouth;
    }
    public boolean isAccessibleFromWest() {
        return accessibleFromWest;
    }
    public void setAccessibleFromWest(boolean accessibleFromWest) {
        this.accessibleFromWest = accessibleFromWest;
    }
    public boolean isAccessibleFromEast() {
        return accessibleFromEast;
    }
    public void setAccessibleFromEast(boolean accessibleFromEast) {
        this.accessibleFromEast = accessibleFromEast;
    }
    public String getGeneralLocation() {
        return generalLocation;
    }
    public void setGeneralLocation(String generalLocation) {
        this.generalLocation = generalLocation;
    }
    public int getItemId() {
        return itemId;
    }
    public void setItemId(int itemId) {
        this.itemId = itemId;
    }
    public int getCharacterId() {
        return characterId;
    }

    public void setCharacterId(int characterId) {
        this.characterId = characterId;
    }
    public int getChanceOfDeath() {
        return chanceOfDeath;
    }
    public void setChanceOfDeath(int chanceOfDeath) {
        this.chanceOfDeath = chanceOfDeath;
    }
    public String getDeathString() {
        return deathString;
    }

    public void setDeathString(String deathString) {
        this.deathString = deathString;
    }
    public String getUserLookPrompt() {
        return userLookPrompt;
    }
    public void setUserLookPrompt(String userLookPrompt) {
        this.userLookPrompt = userLookPrompt;
    }
      public boolean isAccessibility() {
        return accessibility;
    }

    public void setAccessibility(boolean accessibility) {
        this.accessibility = accessibility;
    }

}
