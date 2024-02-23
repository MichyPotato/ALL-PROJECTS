/* Michelle Luo
 * Cmdr. Schenk
 * October 19th
 * AP CSA
 * Character POCO Class
 */

package luo.seven;

public class Character {
    //Fields
    private int characterId;
    private String characterName;
    private String characterPrompt;
    private int itemNeeded;
    private boolean isDefeated;
    private boolean isGateKeeper;
    private String undefeatedPrompt;
    private String defeatedPrompt;

    //Constructor Default
    public Character(){
        this.characterId = 0;
        this.characterName = "";
        this.characterPrompt = "";
        this.itemNeeded = 0;
        this.isDefeated = true;
        this.isGateKeeper = false;
        this.undefeatedPrompt = "";
        this.defeatedPrompt = "";
    }
    //Constructor Partial
    public Character(int characterId, String characterName, String characterPrompt,int itemNeeded){
        this.characterId = characterId;
        this.characterName = characterName;
        this.characterPrompt = characterPrompt;
        this.itemNeeded = itemNeeded;
        this.isDefeated = true;
        this.isGateKeeper = false;
        this.undefeatedPrompt = "";
        this.defeatedPrompt = "";
    }
    //Constructor Full
    public Character(int characterId, String characterName, String characterPrompt,int itemNeeded, boolean isDefeated, boolean isGateKeeper, String undefeatedPrompt, String defeatedPrompt){
        this.characterId = characterId;
        this.characterName = characterName;
        this.characterPrompt = characterPrompt;
        this.itemNeeded = itemNeeded;
        this.isDefeated = isDefeated;
        this.isGateKeeper = isGateKeeper;
        this.undefeatedPrompt = undefeatedPrompt;
        this.defeatedPrompt = defeatedPrompt;
    }
    //Getters and Setters
    public int getCharacterId() {
        return characterId;
    }
    public void setCharacterId(int characterId) {
        this.characterId = characterId;
    }
    public String getCharacterName() {
        return characterName;
    }
    public void setCharacterName(String characterName) {
        this.characterName = characterName;
    }
    public String getCharacterPrompt() {
        return characterPrompt;
    }
    public void setCharacterPrompt(String characterPrompt) {
        this.characterPrompt = characterPrompt;
    }
    public int getItemNeeded() {
        return itemNeeded;
    }
    public void setItemNeeded(int itemNeeded) {
        this.itemNeeded = itemNeeded;
    }
    public boolean isDefeated() {
        return isDefeated;
    }
    public void setDefeated(boolean isDefeated) {
        this.isDefeated = isDefeated;
    }
    public boolean isGateKeeper() {
        return isGateKeeper;
    }
    public void setGateKeeper(boolean isGateKeeper) {
        this.isGateKeeper = isGateKeeper;
    }
    public String getUndefeatedPrompt() {
        return undefeatedPrompt;
    }
    public void setUndefeatedPrompt(String undefeatedPrompt) {
        this.undefeatedPrompt = undefeatedPrompt;
    }
    public String getDefeatedPrompt() {
        return defeatedPrompt;
    }
    public void setDefeatedPrompt(String defeatedPrompt) {
        this.defeatedPrompt = defeatedPrompt;
    }

}
