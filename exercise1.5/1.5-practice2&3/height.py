class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        # Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Adding them up
        total_height_inches = height_A_inches + height_B_inches

        # Getting the output in feet
        output_feet = total_height_inches // 12

        # Getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

    def __sub__(self, other):
        # Convering both objects' heights into inches
        height_C_inches = self.feet * 12 + self.inches
        height_D_inches = other.feet * 12 + other.inches

        # Subtract D from C
        diff_height_inches = height_C_inches - height_D_inches

        # Getting output in feet
        output_feet = diff_height_inches // 12

        # Getting output in inches
        output_inches = diff_height_inches - (output_feet * 12)

        # returning final output as new Height object
        return Height(output_feet, output_inches)

    def __lt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet * 12 + other.inches
        return height_A_inches < height_B_inches

    def __le__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet * 12 + other.inches
        return height_A_inches <= height_B_inches

    def __eq__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet * 12 + other.inches
        return height_A_inches == height_B_inches

    def __gt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet * 12 + other.inches
        return height_A_inches > height_B_inches

    def __ge__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet * 12 + other.inches
        return height_A_inches >= height_B_inches

    def __ne__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = self.feet * 12 + other.inches
        return height_A_inches != height_B_inches

# person_A_height = Height(5, 10)
# person_B_height = Height(4, 10)
# height_sum = person_A_height + person_B_height

# print("Total height:", height_sum)

# person_C_height = Height(5, 10)
# person_D_height = Height(3, 9)
# height_diff = person_C_height - person_D_height

# print("Diff in height: ", height_diff)
