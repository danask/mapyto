import random
import string
import webbrowser

from geopy.geocoders import Nominatim
from math import radians, acos, sin, cos


class Mapyto:
    def __init__(self, lst=["none"], mode=""):
        self.coordinates_list = []
        self.url = ""

        self.main(lst, mode)

    #User agent (= key) generator
    def _user_agent_generator(self, stringLength=8):
        """Generate a random API key for Nominatim

            Arguments:
                stringLength {int} -- Length of the key

            Returns:
                string -- The random API key
            """

        #Create and return a random key
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    #Coordinates list generator
    def get_coordinates(self, address_lst):
        """Generate the list of coordinates

            Arguments:
                adress_lst {list} -- List of addresses

            Returns:
                coordinate_lst -- The list of coordinates
            """

        # Creation of the coordinates list
        for adress in address_lst:
            #Create key
            key = self._user_agent_generator(10)

            #Get coordinates
            geolocator = Nominatim(user_agent=key, timeout=3)
            location = geolocator.geocode(adress)

            #Update the coordinates list
            self.coordinates_list.append([location.latitude, location.longitude])

    #"Distance between coordinates" calculator
    def get_distance(self, a, b, c, d):
        """Convert coordinate into a distance in meters

            Arguments:
                a {int} -- Coordinate x_a
                b {int} -- Coordinate y_a
                c {int} -- Coordinate x_b
                d {int} -- Coordinate y_b

            Returns:
                int -- Distance in meters
            """

        # Conversion of each coordinate into radians
        x_a = radians(a)
        x_b = radians(c)
        y_a = radians(b)
        y_b = radians(d)

        # Calculation of the distance in meters
        distance = 6378137 * acos((sin(x_a) * sin(x_b)) + (cos(x_a) * cos(x_b) * cos(y_b - y_a)))

        return distance

    #The most useful function, the one who sort all of the coordinates/addresses
    def sort_addresses(self):
        """Sorting "near by near" of each coordinates

            Arguments:
                lst {list} -- List of the coordinates

            Returns:
                list -- List of the sorted coordinates
            """

        # Initialisation of local variables
        lst_trans = []
        lst_final = []
        i = 1
        j = 0

        # While loop (= to be sure that all of the list is sorted)
        while self.coordinates_list:
            x = len(self.coordinates_list)

            # Creation of an array = [[distance][coordinate]]
            for i in range(1, x):
                lst_1 = self.coordinates_list[0]
                lst_2 = self.coordinates_list[i]
                z = self.get_distance(lst_1[0], lst_1[1], lst_2[0], lst_2[1])
                lst_trans.append([[round(z)], self.coordinates_list[i]])

            # Sorting of the array
            lst_end = sorted(lst_trans, key=lambda colonne: colonne[0])

            # Preparation of the next loop (delete the first value and throw at the begginning the most close value)
            if len(lst_end) != 0:
                lst_final.append(self.coordinates_list[0])
                self.coordinates_list.pop(0)
                x = lst_end[0][1]
                self.coordinates_list.remove(lst_end[0][1])
                self.coordinates_list.append(x)
                self.coordinates_list.reverse()
            else:
                lst_final.append(self.coordinates_list[0])
                break

            # Erasing of the local variable for next loop
            lst_end = []
            lst_trans = []

            j += 1

        return lst_final

    #Main function
    def main(self, lst=["none"], mode=""):
        """Main function

                    Arguments:
                        lst {list} -- List of the adresses - if ['none'] launch the input
                        mode {str} -- is mode != "" - then it will just return the final link instead of open it in the
                        web browser

                    Returns:
                        link -- The optimized itinerary Google Maps url
                    """

        #Check if an adress list has been give to the function
        if lst == ["none"] :
            #Adress list generator with inputs
            nbr = int(input("How many adresses do you have to enter ? "))
            adresses_list = []
            for i in range(nbr):
                adress = input(f"Adress n°{i+1} : ")
                adresses_list.append(adress)
        else:
            adresses_list = lst

        #Get the coordinates of the addresses list
        self.get_coordinates(adresses_list)

        #Sort the coordinates
        sorted_coordinates = self.sort_addresses()

        #Initialisation of the url var
        url_bgn = "https://www.google.com/maps/dir"
        link_end = ""

        #Creation of the url
        for i, j in sorted_coordinates:
            link_end += "/" + str(i) + "," + str(j)
        url_end = url_bgn + link_end

        #Check the mode
        if mode == "":
            #Open the url in the web browser
            webbrowser.open(url_end)
        else:
            #Return the url
            self.url = url_end
