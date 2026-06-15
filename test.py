def navigate_drone(starting_coordinate, instructions):
    # Write your code below
    x, y, z = starting_coordinate[0], starting_coordinate[1], starting_coordinate[2]
    total_movement = 0
    leftspace = 0

    # Process each instruction
    for instruction in instructions:
        distance = int(instruction[:-1])  # Extract the distance part of the instruction
        direction = instruction[-1]       # Extract the direction part of the instruction

        # Update coordinates based on direction
        if direction == 'N':

            if total_movement + distance > 1000:
                leftspace = 1000 - total_movement
                total_movement += leftspace
                y += leftspace
                print("In not be be loop N")
                break
            else:
                print("Befor Y", y, "\n")
                y += distance
                print("After Y", y, "\n")

        elif direction == 'S':
            if total_movement + distance >= 1000:
                leftspace = 1000 - total_movement
                total_movement += leftspace
                y -= leftspace
                print("In not be be loop S")
                break
            else:
                print("Befor Y", y, "\n")
                y -= distance
                print("After Y", y, "\n")

        elif direction == 'E':
            if total_movement + distance >= 1000:
                leftspace = 1000 - total_movement
                total_movement += leftspace
                x += leftspace
                print("In not be be loop E")
                break
            else:
                print("Befor Y", y, "\n")
                x += distance
                print("After Y", y, "\n")

        elif direction == 'W':
            if total_movement + distance >= 1000:
                leftspace = 1000 - total_movement
                total_movement += leftspace
                x -= leftspace
                print("In not be be loop W")
                break
            else:
                print("Befor X", x, "\n")
                x -= distance
                print("After X", x, "\n")

        elif direction == 'U':
            if total_movement + distance >= 1000:
                leftspace = 1000 - total_movement
                total_movement += leftspace
                z += leftspace
                print("In not be be loop U")
                break
            else:
                print("Befor Z", z, "\n")
                z += distance
                print("After Z", z, "\n")

        elif direction == 'D':
            if total_movement + distance >= 1000:
                leftspace = 1000 - total_movement
                total_movement += leftspace
                z -= leftspace
                print("In not be be loop D")
                break
            else:
                print("Befor Z", z, "\n")
                z -= distance
                print("After Z", z, "\n")

        if total_movement + distance > 1000:
            leftspace = 1000 - total_movement
            total_movement += leftspace
            break
        else:
            # Update total movement
            total_movement += abs(distance)

        # Stop if total movement reaches 1000
        if total_movement >= 1000:
            break

    return [x, y, z]


if __name__ == '__main__':
    starting_coordinate = [4, 3, 0]
    instructions = ['-700N', '-400E', '200U', '200S', '200S', '300E', '200D']
    print(navigate_drone(starting_coordinate, instructions))


else:
    if distance > 0:
        print("Befor Y", y, "\n")
        y += distance
        print("After Y", y, "\n")
    else:
        y -= abs(distance)