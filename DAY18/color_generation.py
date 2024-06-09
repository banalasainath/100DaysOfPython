import colorgram

colors = colorgram.extract('hirst_spot_painting.jpg', 10)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    if color_tuple[0] > 220 and color_tuple[1] > 220 and color_tuple[2] > 220:
        pass
    else:
        rgb_colors.append(color_tuple)

final_colors = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (141, 178, 204), (139, 82, 105)]
