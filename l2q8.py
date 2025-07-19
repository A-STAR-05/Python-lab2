playcric={1,2,3,5,6,7,8,10}
playfootball={1,2,3,10}
university={1,2,3,4,5,6,7,8,9,10}
print("Players who play both cricket and football:", playcric & playfootball)
print("PLAYER who play only one sport:",playcric ^ playfootball)
print("Players who play neither sport:", university-(playcric | playfootball))
