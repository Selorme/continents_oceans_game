import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Ariel", 8, "normal")
screen = turtle.Screen()
screen.title("Continents and Oceans Game")

image = "world_map.gif"
screen.addshape(image)
turtle.shape(image)

screen.setup(1415, 815)

place = ["North America", "South America", "Pacific Ocean", "Africa", "Asia", "Europe", "Australasia",
         "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean", "Antarctica"]
x_cor = [-520.0, -389.0, -589.0, 9.0, 278.0, -53.0, 517.0, -307.0, 228.0, -30.0, 4.0, 30.0]
y_cor = [222.0, -136.0, -176.0, -3.0, 194.0, 248.0, -226.0, 90.0, -39.0, -318.0, 372.0, -389.0]
place_coordinate = pandas.DataFrame({"Place": place, "x": x_cor, "y": y_cor})
place_coordinate.to_csv("continents_and_oceans.csv")

places_data = pandas.read_csv("continents_and_oceans.csv")
all_places_data = places_data.Place.to_list()
guessed_place = []

while len(guessed_place) < 12:
    answer_place = screen.textinput(title=f"{len(guessed_place)}/12 places correct",
                                    prompt="What's another ocean/continent?").title()
    if answer_place == "Exit":
        missing_place = [place for place in all_places_data if place not in guessed_place]
        new_info = pandas.DataFrame(missing_place)
        new_info.to_csv("continents_and_oceans_to_learn")
        break
    if answer_place in all_places_data:
        guessed_place.append(answer_place)
        writer = turtle.Turtle()
        writer.ht()
        writer.penup()
        place_data = places_data[places_data.Place == answer_place]
        writer.goto(int(place_data.x), int(place_data.y))
        writer.write(answer_place, True, align=ALIGNMENT, font=FONT)
