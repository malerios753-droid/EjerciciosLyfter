class Head:
    def __init__(self, eye_color="brown"):
        self.eye_color = eye_color

class Hand:
    def __init__(self, fingers=5):
        self.fingers = fingers

class Feet:
    def __init__(self, shoe_size=36):
        self.shoe_size = shoe_size

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, name, torso):
        self.name = name
        self.torso = torso



head = Head(eye_color="brown")

right_hand = Hand(fingers=5)
left_hand =  Hand(fingers=5)
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_feet = Feet(shoe_size=40)
left_feet = Feet(shoe_size=40)
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

person = Human(name="Alejandro", torso=torso)


print(f"Nombre: {person.name}")
print(f"Color de ojos: {person.torso.head.eye_color}")
print(f"Dedos en mano derecha: {person.torso.right_arm.hand.fingers}")
print(f"Talla de zapato pie izquierdo: {person.torso.left_leg.feet.shoe_size}")