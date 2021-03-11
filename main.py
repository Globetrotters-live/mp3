import random
import pygame

alltitles = open("titles.txt").read().split("\n")
class MP3:

    instances = set()
    instances: set


    def __init__(self, name, interpret, duration):

        self.name = name
        self.interpret = interpret
        self.duration = duration
        MP3.instances.add(self)

    def add(self):
        for i in self:
            x = i.split("-")
            MP3(x[0], x[1], 1.5)




    @classmethod
    def writetitel(self):
        for i in self.instances:
            print(i.name)

    @classmethod
    def writeduration(self):
        for  i in self.instances:
            print(i.duration)
    @classmethod
    def writeinterpret(self):
        for i in self.instances:
            print(i.interpret)
    @classmethod
    def writeall(self):
        for i in self.instances:
            print(i.name, i.interpret, i.duration)

    @classmethod
    def vypis_cele(self):
        for i in self.instance:
            print(i.name, i.interpret, i.duration)

    @classmethod
    def vyber_skladbu(self):

        for i in self.instances:
            akt_skladba_z = []
            akt_skladba_z.append(i.name)
            akt_skladba_z.append(i.interpret)
            akt_skladba_z.append(i.duration)
            return akt_skladba_z

    akt_skladba_z = []


MP3.add(alltitles)
MP3.writeinterpret()


# pygame časť
Width, Height = 250 , 400
screen = pygame.display.set_mode((Width, Height))


playy=0
playx=0
stopx=0
stopy=80
nextx=0
nexty=160


pygame.display.set_caption("MP3 Player")
playimg = pygame.image.load("play.png")
nextimg = pygame.image.load("next.png")
stopimg = pygame.image.load("stop.png")

pygame.font.init()
akt_skladba_z=MP3.vyber_skladbu()
print(akt_skladba_z)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Play', True,(255,255,255), None)

#nextimg=pygame.image.load("next.png")

def main():
    run = True
    while run:
        text_name = font.render(akt_skladba_z[0], True, (255,255,255) ,None)
        text_interpret = font.render(akt_skladba_z[1], True, (255, 255, 255),None)
        text_duration = font.render(str(akt_skladba_z[2]), True, (255, 255, 255),None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (playx < pos[0] and playx +80 > pos[0] and playy<pos[1] and playy+40 >pos[1]):
                    print('play')
                if (stopx < pos[0] and stopx + 80 > pos[0] and stopy < pos[1] and stopy + 40 > pos[1]):
                    print('stop')
                if (nextx < pos[0] and nextx + 80 > pos[0] and nexty < pos[1] and nexty + 40 >pos[1]):
                    print('next')


        screen.blit(playimg, (0,0))
        screen.blit(stopimg, (0,80))
        screen.blit(nextimg, (0,160))
        screen.blit(text_name,(0,200))
        screen.blit(text_interpret, (0, 240))
        screen.blit(text_duration, (0, 280))


        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()