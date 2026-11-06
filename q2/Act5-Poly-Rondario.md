What do all the methods (move(), special_move(), use()) in the previous activities have in common?

They all share the same method name and purpose across different, independent classes, allowing them to be called uniformly through duck-typing without requiring a shared parent class.


How does this activity show polymorphism in a gaming context?

It demonstrates polymorphism by allowing different game items or characters to implement a common interface method (such as use() or special_move()), enabling a single function or loop to trigger unique, object-specific behaviors without needing to check the object's class type.


Can you think of other examples where the same action behaves differently depending on the character or item?

An example is an interact() method where a player opens a door, an NPC initiates dialogue, and a chest triggers a loot inventory popup. Another common example is an attack() method where a warrior performs a melee strike, a mage casts a spell, and an archer fires a ranged shot.