
from __future__ import print_function
import sys

choices = [ ]

for x in range( 0, 9 ):
    choices.append( str( x + 1 ) )

playerOneTurn = True
winner = False


def printBoard():
    print( '\n -----' )
    print( '|' + choices[ 0 ] + '|' + choices[ 1 ] + '|' + choices[ 2 ] + '|' )
    print( ' -----' )
    print( '|' + choices[ 3 ] + '|' + choices[ 4 ] + '|' + choices[ 5 ] + '|' )
    print( ' -----' )
    print( '|' + choices[ 6 ] + '|' + choices[ 7 ] + '|' + choices[ 8 ] + '|' )
    print( ' -----\n' )


count = 0
while not winner:

    printBoard()

        print("kazandın")
    if (count >= 9):
        print( "Berabere" )
        sys.exit()
    if playerOneTurn:
        print( "Oyuncu 1:" )
    else:
        print( "Oyuncu 2:" )

    try:
        choice = int( input( " " ) )
    except:
        print( "Sayi:" )
        continue
    if (choice > 9):
        sys.exit()
    if choices[ choice - 1 ] == 'X' or choices[ choice - 1 ] == 'O':
        print( "Yanlıs sayi" )
        continue

    if playerOneTurn:
        count += 1
        choices[ choice - 1 ] = 'X'
    else:
        count += 1
        choices[ choice - 1 ] = 'O'

    playerOneTurn = not playerOneTurn


print( "Oyuncu " + str( int( playerOneTurn + 1 ) ) + " Kazanan!\n" )