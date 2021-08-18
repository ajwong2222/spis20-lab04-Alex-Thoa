import turtle
snowflaketurtle = turtle.Turtle()

def snowflake(side_length, levels): 

# this recursion draws snowflake_side three times turning to make a snowflake.

    snowflake_side (side_length, levels) 

    snowflaketurtle.right (120)

    snowflake_side (side_length, levels)

    snowflaketurtle.right (120)

    snowflake_side (side_length, levels)

    snowflaketurtle.right (120)

def snowflake_side (side_length, levels):

# base case where nothing should happen

    if levels == 0:

        snowflaketurtle.forward (side_length)

        return

    else: 

        #this recursion essentially draws a series of nested triangles that create a side

        snowflaketurtle.speed(10)

        snowflaketurtle.pendown()

        snowflake_side (side_length // 3, levels - 1)

        snowflaketurtle.left (60)

        snowflake_side (side_length // 3, levels - 1)

        snowflaketurtle.right (120)

        snowflake_side (side_length // 3, levels - 1)

        snowflaketurtle.left (60)

        snowflake_side (side_length // 3, levels - 1)

        # snowflaketurtle.left (60)

# snowflake_side (200, 3)

snowflake (200, 3)
        
        
    
