from config import CANVAS_HEIGHT_INIT, CANVAS_WIDTH_INIT, DIFFICULTY_LEVEL_INIT
import game, sys, getopt



def main(argv):

    canvas_height = CANVAS_HEIGHT_INIT
    canvas_width = CANVAS_WIDTH_INIT
    difficulty_level = DIFFICULTY_LEVEL_INIT

    # This block checks and gets valid arguments
    try:
      opts, args = getopt.getopt(argv,"h:w:d:",["canvas_height=","canvas_width=","difficulty_level="])
    except getopt.GetoptError:
      print ('__main__.py -h <canvas_height> -w <canvas_width> -d <difficulty-level>')
      sys.exit(2)

    for opt, arg in opts:
      if opt in ("-h", "--canvas_height"):
          canvas_height = arg
          
      elif opt in ("-w", "--canvas_width"):
          canvas_width = arg
      
      elif opt in ("-d", "--difficulty_level"):
          difficulty_level = arg

    # Run the game
    game.run(canvas_height, canvas_width, difficulty_level)
    
if __name__ == '__main__':

    main(sys.argv[1:])