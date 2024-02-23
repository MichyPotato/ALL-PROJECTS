/* Michelle Luo
 * Cmdr. Schenk
 * October 19th
 * AP CSA
 * Item POCO Class
 */

package luo.seven;

public class Item {
    //Fields
    private int itemId;
    private String itemName;
    private String itemOnGroundPrompt;
    private OnInventory onInventory;
    private int thingsContainedWithin;
    //Constructor Default
    public Item(){
        this.itemId = 0;
        this.itemName = "";
        this.itemOnGroundPrompt = "";
        this.onInventory = OnInventory.onGround;
    }
    //Constructor Partial
    public Item(int itemId){
        this.itemId = itemId;
        this.itemName = "";
        this.itemOnGroundPrompt = "";
        this.onInventory = OnInventory.onGround;
    }
    // Constructor Full
    public Item(int itemId, String itemName, String itemOnGroundPrompt, OnInventory onInventory, int thingsContainedWithin){
        this.itemId = itemId;
        this.itemName = itemName;
        this.itemOnGroundPrompt = itemOnGroundPrompt;
        this.onInventory = onInventory;
        this.thingsContainedWithin = thingsContainedWithin;
    }
    // Getters and Setters
    public int getItemId() {
        return itemId;
    }
    public void setItemId(int itemId) {
        this.itemId = itemId;
    }
    public String getItemName() {
        return itemName;
    }
    public void setItemName(String itemName) {
        this.itemName = itemName;
    }
    public String getItemOnGroundPrompt() {
        return itemOnGroundPrompt;
    }
    public void setItemOnGroundPrompt(String itemOnGroundPrompt) {
        this.itemOnGroundPrompt = itemOnGroundPrompt;
    }
    public OnInventory getOnInventory() {
        return onInventory;
    }
    public void setOnInventory(OnInventory onInventory) {
        this.onInventory = onInventory;
    }
    public int getThingsContainedWithin() {
        return thingsContainedWithin;
    }
    public void setThingsContainedWithin(int thingsContainedWithin) {
        this.thingsContainedWithin = thingsContainedWithin;
    }
}
