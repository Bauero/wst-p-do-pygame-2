# Import modułu
import pygame
 
# inicjalizacja modułu
pygame.init()
 
# Utworzenie zmiennych okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
# nadaję nazwę oknu
pygame.display.set_caption('Pierwsza Gra')
 
# tworzę zmienną o nazwie screen_surface, do której zapiszemy całe okienko gry
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def load_image(img_path, position):

    image = pygame.image.load(img_path)
    surface = image.convert()

    #z obrazka wycinamy (robimy transparentnym) ten kolor
    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect( center = position )

    return [image, surface, rect]

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image("player.png",player_pos)
background_color = [0,0,0]


def print_image(img_lista):

    image, surface, rect = img_lista

    screen_surface.blit(surface, rect)


def set_position_image(img_list, position):

    image, surface, rect = img_list

    rect = surface.get_rect( center = position )

    return [image, surface, rect]

#przeliczanie pozycji gracza
def calculate_player_movement(keys):

    speed = 10
    zmiana_x = 0
    zmiana_y = 0
 
    if keys[pygame.K_w]:
        zmiana_y -= speed
    if keys[pygame.K_s]:
        zmiana_y += speed
    if keys[pygame.K_d]:
        zmiana_x += speed
    if keys[pygame.K_a]:
        zmiana_x -= speed

    return [zmiana_x, zmiana_y]

def limit_position(position):
    x , y = position

    x = max(0, min(x,SCREEN_WIDTH))
    y = max(0, min(y,SCREEN_HEIGHT))

    return [x,y]


# tworzymy zmienną, która przechowuje stan gry (czyli czy gra działa czy nie działa)
game_status = True
 
# tworzę zmienną o nazwie clock i przypisuję do niej obiekt zegara
clock = pygame.time.Clock()
 
# Kod wykonywany dopóki aplikacja jest uruchomiona
while game_status:
    # Odczytywanie zdarzeń zarejestrowanych przez komputer
    # zdarzenie jest to jakakolwiek interakcja użytkownika z grą np. ruch myszką
    events = pygame.event.get()
 
    # tworzę pętlę for po events (czyli tablicy zdarzeń)
    # iteruję zdarzenie po zdarzeniu i wyświetlam każde zdarzenie - print(event)
    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            game_status = False

        pressed_keys = pygame.key.get_pressed()

        przes_x, przes_y = calculate_player_movement(pressed_keys)

        player_pos[0] += przes_x
        player_pos[1] += przes_y

        player_pos = limit_position(player_pos)

        player = set_position_image(player, player_pos)


    screen_surface.fill(background_color)
    
    #ładowanie naszego gracza na ekran
    print_image(player)

    # odświeżamy wyświetlane okienko
    pygame.display.update()

    clock.tick(60)

print("Gra została zakończona")

pygame.quit()
quit()
