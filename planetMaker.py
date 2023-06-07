from PIL import Image
import random 

def generateImage(steps):
    '''
    créé une fusion de toutes les images
    @entrée:une liste 
    '''
    # Open Images
    BACKGROUND = Image.open('assets/planets/color_' + str(random.randint(1,4)) + '/' + steps[0])
    FRONT =  Image.open('assets/planets/color_' + str(random.randint(1,4)) + '/' + steps[1])

    # Calculate width to be at the center
    width = (BACKGROUND.width - FRONT.width) // 2
    # Calculate height to be at the center
    height = (BACKGROUND.height - FRONT.height) // 2

    # Paste the frontImage at (width, height)
    BACKGROUND.paste(FRONT, (width, height), FRONT)
      
    # Save this image
    BACKGROUND.save("assets/planets/stock/s1/1.png", format="png")


    for i in range(1,len(steps)-2):

        # Open Images
        BACKGROUND = Image.open('assets/planets/stock/s' + str(i) + '/1.png')
        FRONT =  Image.open('assets/planets/color_' + str(random.randint(1,4)) + '/' + steps[i+1])



        # Paste the frontImage at (width, height)
        BACKGROUND.paste(FRONT, (0,0), FRONT)
      
        # Save this image
        BACKGROUND.save("assets/planets/stock/s" + str(i+1) + '/1.png', format="png")