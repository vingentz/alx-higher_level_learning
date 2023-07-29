#!/usr/bin/python3

"""first class base"""

import json
import csv
import turtle


class Base:
    """super class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string rep of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string rep of list_objs to file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string rep json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            testcpy = cls(1, 1)
        else:
            testcpy = cls(1)
        testcpy.update(**dictionary)
        return (testcpy)

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in list]
        except FileNotFoundError:
                return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves list of objects to CSV file"""
        filename = cls.__name__ + ".csv"  # creates a filename for the CSV file
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")  # Return an empty list
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """read data from CSV file & return list of instantiated classes"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                # read data from CSV file
                list = csv.DictReader(file, fieldnames=fieldnames)
                # convert read dictionaries into list of dictionaries
                list = [dict([k, int(v)] for k, v in d.items())
                        for d in list]
                return [cls.create(**d) for d in list]
        except IOError:
                return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles & Squares using turtle module.
        Args:
        list_rectangles : A list of Rectangle objects to draw.
        list_squares : A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
