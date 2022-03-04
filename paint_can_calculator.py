#number of cans to spray paint a wall, knowing a can covers up 5 m^2, and giving the height and the lenght of the wall as an input
import math
def paint_calc(height, width, cover):
    total_cans = math.ceil(height * width / cover)
    print(f"You need {total_cans} cans of paint")



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
