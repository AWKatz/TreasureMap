# This is Day 4 of 100 for the Udemy Python Bootcamp

row1 = ["🟨", "🟨", "🟨"]
row2 = ["🟨", "🟨", "🟨"]
row3 = ["🟨", "🟨", "🟨"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("At which coordinates do you want to hide the treasure?(column # and row #) ")

# select the column
horizontal = int(position[0])
# select the row
vertical = int(position[1])

# update position with an X
treasure = (map[vertical - 1])
treasure[horizontal - 1] = "❌"

# redraw the map
print(f"{row1}\n{row2}\n{row3}")
