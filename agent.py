import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()
pygame.font.init()

# Game Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
COLOR_GROUND = (34, 139, 34)      # Dark Grass
COLOR_ROAD = (44, 62, 80)          # Asphalt
COLOR_BUILDING = (127, 140, 141)  # Concrete Gray
COLOR_PLAYER = (52, 152, 219)     # Tommy AI (Blue)
COLOR_POLICE = (231, 76, 60)      # Police (Red)
COLOR_CIVILIAN = (241, 196, 15)   # Pedestrian (Yellow)
COLOR_CAR = (142, 68, 173)        # Hijackable Car (Purple)
COLOR_TEXT = (236, 240, 241)

class GameUI:
    def __init__(self):
        self.font_large = pygame.font.SysFont("Impact", 36)
        self.font_medium = pygame.font.SysFont("Arial", 16, bold=True)
        self.font_small = pygame.font.SysFont("Courier New", 12)

    def draw_hud(self, screen, player, wanted_level, mission_text, is_ai, ai_objective, bullets, cops, timer):
        # Top Left: Status & AI Modes
        mode_text = "🤖 AI AUTOPILOT MODE" if is_ai else "🎮 MANUAL PLAYER CONTROL"
        mode_color = (46, 204, 113) if is_ai else (52, 152, 219)
        lbl_mode = self.font_large.render(mode_text, True, mode_color)
        screen.blit(lbl_mode, (20, 20))

        lbl_objective = self.font_medium.render(f"🤖 AGENT OBJECTIVE: {ai_objective.upper()}", True, (241, 196, 15))
        screen.blit(lbl_objective, (20, 60))

        # Top Right: Vital stats / GTA wanted system
        lbl_health = self.font_large.render(f"❤️ HEALTH: {int(player.health)}", True, (231, 76, 60))
        screen.blit(lbl_health, (SCREEN_WIDTH - 250, 20))

        # Wanted Level
        stars = "⭐" * wanted_level if wanted_level > 0 else "CASUAL"
        lbl_wanted = self.font_large.render(f"WANTED: {stars}", True, (241, 196, 15) if wanted_level > 0 else (189, 195, 199))
        screen.blit(lbl_wanted, (SCREEN_WIDTH - 250, 60))

        # Bottom UI Overlay: Mission Box
        box_rect = pygame.Rect(20, SCREEN_HEIGHT - 120, SCREEN_WIDTH - 40, 95)
        pygame.draw.rect(screen, (0, 0, 0, 180), box_rect)
        pygame.draw.rect(screen, mode_color, box_rect, 2)

        lbl_mission = self.font_medium.render(f"🎯 MISSION STATUS: {mission_text}", True, COLOR_TEXT)
        screen.blit(lbl_mission, (35, SCREEN_HEIGHT - 110))

        controls_hint = "[TAB] Toggle Auto-AI Agent | [SPACE] Open Fire | [F] Jack Car | [W/A/S/D] Movement"
        lbl_controls = self.font_small.render(controls_hint, True, (149, 165, 166))
        screen.blit(lbl_controls, (35, SCREEN_HEIGHT - 45))

        # Instructions Console
        lbl_input_prompt = self.font_small.render("💬 Type into Terminal Window to Issue Natural commands like 'survive', 'fight cops', 'steal'", True, (241, 196, 15))
        screen.blit(lbl_input_prompt, (35, SCREEN_HEIGHT - 75))

class Bullet:
    def __init__(self, x, y, target_x, target_y, is_police=False):
        self.x = x
        self.y = y
        self.is_police = is_police
        self.speed = 10
        angle = math.atan2(target_y - y, target_x - x)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed
        self.range = 40

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.range -= 1
        return self.range > 0

    def draw(self, screen):
        color = (241, 196, 15) if not self.is_police else (255, 255, 255)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 3)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dx = random.uniform(-3, 3)
        self.dy = random.uniform(-3, 3)
        self.lifetime = random.randint(15, 30)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1
        return self.lifetime > 0

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), random.randint(2, 5))

class Entity:
    def __init__(self, x, y, color, speed=3):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.health = 100
        self.radius = 12
        self.in_car = False
        self.car_entity = None

    def distance_to(self, target):
        return math.hypot(target.x - self.x, target.y - self.y)

    def move_towards(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        spd = self.speed * 2.5 if self.in_car else self.speed
        self.x += math.cos(angle) * spd
        self.y += math.sin(angle) * spd

    def draw(self, screen):
        if self.in_car:
            # Draw Car outline enclosing agent
            pygame.draw.rect(screen, self.color, (int(self.x - 20), int(self.y - 12), 40, 24), 0, 4)
            pygame.draw.rect(screen, (44, 62, 80), (int(self.x - 10), int(self.y - 8), 12, 16)) # windshield
        else:
            # Pedestrian
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, (44, 62, 80), (int(self.x + 4), int(self.y - 4)), 2) # Details

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice([(142, 68, 173), (230, 126, 34), (22, 160, 133), (127, 140, 141)])
        self.radius = 20
        self.occupied = False

    def draw(self, screen):
        if not self.occupied:
            pygame.draw.rect(screen, self.color, (int(self.x - 20), int(self.y - 12), 40, 24), 0, 4)
            pygame.draw.rect(screen, (52, 73, 94), (int(self.x - 8), int(self.y - 8), 16, 16), 2)

class CityMap:
    def __init__(self):
        # Road Network layout
        self.roads = [
            pygame.Rect(0, 150, SCREEN_WIDTH, 70),
            pygame.Rect(0, 450, SCREEN_WIDTH, 70),
            pygame.Rect(200, 0, 70, SCREEN_HEIGHT),
            pygame.Rect(700, 0, 70, SCREEN_HEIGHT)
        ]
        # Solid Concrete building blocks
        self.buildings = [
            pygame.Rect(50, 30, 100, 90),
            pygame.Rect(320, 30, 150, 90),
            pygame.Rect(820, 30, 130, 90),
            pygame.Rect(50, 260, 100, 150),
            pygame.Rect(320, 260, 320, 150),
            pygame.Rect(820, 260, 130, 150),
            pygame.Rect(320, 560, 320, 90)
        ]

    def draw(self, screen):
        # Background
        screen.fill(COLOR_GROUND)
        # Roads
        for road in self.roads:
            pygame.draw.rect(screen, COLOR_ROAD, road)
            # Dashed lines
            if road.width > road.height:
                for x in range(0, SCREEN_WIDTH, 40):
                    pygame.draw.line(screen, (255, 255, 255), (x, road.centery), (x+15, road.centery), 2)
            else:
                for y in range(0, SCREEN_HEIGHT, 40):
                    pygame.draw.line(screen, (255, 255, 255), (road.centerx, y), (road.centerx, y+15), 2)
        # Buildings
        for bld in self.buildings:
            pygame.draw.rect(screen, COLOR_BUILDING, bld)
            pygame.draw.rect(screen, (50, 50, 50), bld, 2)

class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("GTA 6 : AI Autonomous Agent Sandbox 0.6")
        self.clock = pygame.time.Clock()
        self.running = True

        self.city = CityMap()
        self.ui = GameUI()

        # Set up Player AI and open-world entities
        self.player = Entity(100, 200, COLOR_PLAYER, speed=2.5)
        self.cops = [Entity(random.randint(500, 900), random.randint(300, 600), COLOR_POLICE, speed=2) for _ in range(3)]
        self.civilians = [Entity(random.randint(50, 950), random.randint(50, 650), COLOR_CIVILIAN, speed=1.5) for _ in range(8)]
        self.cars = [Car(300, 185), Car(735, 200), Car(235, 485), Car(850, 485)]

        self.bullets = []
        self.particles = []
        
        self.wanted_level = 1
        self.ai_agent_enabled = True # Start in interactive AI Agent autopilot
        self.ai_objective = "survive and navigate"
        self.mission_status = "Infiltrate Liberty Suburb. Hijack purple wheels or fight patrol squads."
        self.timer = 0

    def trigger_explosion(self, x, y, color=(230, 126, 34)):
        for _ in range(15):
            self.particles.append(Particle(x, y, color))

    def user_commands_listener(self):
        # Allow interactive command overrides directly via standard console terminal
        import threading
        def get_console_commands():
            while self.running:
                cmd = input("📟 [Agent Overlord Shell] Define Current Target: ").strip().lower()
                if cmd in ["survive", "roam", "flee", "fight cops", "steal car", "die"]:
                    self.ai_objective = cmd
                    print(f"🤖 Agent Commander override processed! Target changed: {cmd.upper()}")
                else:
                    print("⚠️ Command unregistered. Use: 'survive', 'fight cops', 'steal car', 'flee', 'roam'.")
        t = threading.Thread(target=get_console_commands, daemon=True)
        t.start()

    def run(self):
        self.user_commands_listener()
        while self.running:
            self.clock.tick(FPS)
            self.timer += 1
            self.handle_events()
            self.update_game()
            self.render()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.ai_agent_enabled = not self.ai_agent_enabled
                    self.ai_objective = "flee and survive" if self.ai_agent_enabled else "manual"
                elif event.key == pygame.K_f:
                    # manual hijack attempt
                    for car in self.cars:
                        if not car.occupied and self.player.distance_to(car) < 40:
                            self.player.in_car = True
                            car.occupied = True
                            self.player.color = car.color
                            self.trigger_explosion(self.player.x, self.player.y, (189, 195, 199))
                            self.wanted_level = min(5, self.wanted_level + 1)
                            self.mission_status = "Grand Theft Success! Autopilot triggered chase response."

    def update_game(self):
        # AI Logic State-Machine
        if self.ai_agent_enabled:
            self.ai_agent_logic()
        else:
            self.manual_movement()

        # Boundary controls
        self.player.x = max(15, min(SCREEN_WIDTH - 15, self.player.x))
        self.player.y = max(15, min(SCREEN_HEIGHT - 15, self.player.y))

        # Cops tracking Tommy AI Agent
        for cop in self.cops:
            # Speed boosts depending on wanted levels
            cop.speed = 1.5 + (self.wanted_level * 0.4)
            if cop.distance_to(self.player) < 300:
                cop.move_towards(self.player.x, self.player.y)
                
                # Shot patterns
                if random.random() < 0.02:
                    self.bullets.append(Bullet(cop.x, cop.y, self.player.x, self.player.y, is_police=True))

            # Melee damage
            if cop.distance_to(self.player) < 15:
                self.player.health -= 0.5
                if random.random() < 0.1:
                    self.trigger_explosion(self.player.x, self.player.y, (192, 57, 43))

        # Update and boundary check bullets
        self.bullets = [b for b in self.bullets if b.update()]
        self.particles = [p for p in self.particles if p.update()]

        # Hit Detection & System Rules
        for bullet in self.bullets:
            if bullet.is_police:
                if math.hypot(bullet.x - self.player.x, bullet.y - self.player.y) < self.player.radius:
                    self.player.health -= 5
                    self.trigger_explosion(self.player.x, self.player.y, (231, 76, 60))
                    bullet.range = 0
            else:
                for cop in self.cops:
                    if math.hypot(bullet.x - cop.x, bullet.y - cop.y) < cop.radius:
                        cop.health -= 35
                        self.trigger_explosion(cop.x, cop.y, (192, 57, 43))
                        bullet.range = 0
                        if cop.health <= 0:
                            self.cops.remove(cop)
                            self.wanted_level = min(5, self.wanted_level + 1)
                            self.mission_status = "Cop Down! Search Squad reinforcements dispatched."
                            # respawn backup cops
                            self.cops.append(Entity(random.choice([0, SCREEN_WIDTH]), random.choice([0, SCREEN_HEIGHT]), COLOR_POLICE))

        # Respawn lost target items
        if len(self.cops) < self.wanted_level + 1:
            self.cops.append(Entity(random.choice([0, SCREEN_WIDTH]), random.choice([0, SCREEN_HEIGHT]), COLOR_POLICE))

        # Player death sequence check
        if self.player.health <= 0:
            self.trigger_explosion(self.player.x, self.player.y, (192, 57, 43))
            self.player.x, self.player.y = 100, 200
            self.player.health = 100
            self.player.in_car = False
            self.player.color = COLOR_PLAYER
            self.wanted_level = 1
            self.mission_status = "BUSTED / WASTED! Restarting AI Agent in stealth mode."

    def manual_movement(self):
        keys = pygame.key.get_pressed()
        spd = self.player.speed * 2.5 if self.player.in_car else self.player.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.x -= spd
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.x += spd
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player.y -= spd
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player.y += spd

        if keys[pygame.K_SPACE] and self.timer % 8 == 0:
            # manual firing towards closest danger
            if self.cops:
                nearest_cop = min(self.cops, key=lambda c: self.player.distance_to(c))
                self.bullets.append(Bullet(self.player.x, self.player.y, nearest_cop.x, nearest_cop.y))

    def ai_agent_logic(self):
        # AI Autonomous Control Brain
        nearest_cop = min(self.cops, key=lambda c: self.player.distance_to(c)) if self.cops else None
        dist_to_threat = self.player.distance_to(nearest_cop) if nearest_cop else 9999

        # Target behavior transitions based on current AI objective
        if dist_to_threat < 180 and self.ai_objective != "fight cops":
            self.ai_objective = "flee"

        # State Execution
        if self.ai_objective == "flee" and nearest_cop:
            # Escape route planning
            flee_x = self.player.x - (nearest_cop.x - self.player.x)
            flee_y = self.player.y - (nearest_cop.y - self.player.y)
            self.player.move_towards(flee_x, flee_y)
            self.mission_status = "Fleeing hot hostiles. Running from nearest units."

            # Shoot back to cover retreat if too close
            if dist_to_threat < 120 and self.timer % 15 == 0:
                self.bullets.append(Bullet(self.player.x, self.player.y, nearest_cop.x, nearest_cop.y))

            if dist_to_threat > 280:
                self.ai_objective = "steal car" if not self.player.in_car else "roam"

        elif self.ai_objective == "steal car" and not self.player.in_car:
            # Pick the closest vacant vehicle
            available_cars = [c for c in self.cars if not c.occupied]
            if available_cars:
                target_car = min(available_cars, key=lambda c: self.player.distance_to(c))
                self.player.move_towards(target_car.x, target_car.y)
                self.mission_status = f"Locating target auto vehicle at {int(target_car.x)}, {int(target_car.y)}"
                
                # Proximity Hijack Trigger
                if self.player.distance_to(target_car) < 15:
                    self.player.in_car = True
                    target_car.occupied = True
                    self.player.color = target_car.color
                    self.trigger_explosion(self.player.x, self.player.y, (241, 196, 15))
                    self.wanted_level = min(5, self.wanted_level + 1)
                    self.ai_objective = "roam"
            else:
                self.ai_objective = "fight cops"

        elif self.ai_objective == "fight cops" and nearest_cop:
            # Attack tactical movements
            self.player.move_towards(nearest_cop.x, nearest_cop.y)
            self.mission_status = f"Engaging squad units. Wanted rating {self.wanted_level}⭐."
            
            if self.timer % 10 == 0:
                self.bullets.append(Bullet(self.player.x, self.player.y, nearest_cop.x, nearest_cop.y))

            if dist_to_threat < 60:
                # Disengage if critical health
                if self.player.health < 30:
                    self.ai_objective = "flee"

        else: # Roaming/patrolling Sandbox State
            self.mission_status = "Observing sandbox. Patrolling metropolitan routes."
            if self.timer % 120 == 0:
                # Make random wander points
                self.wander_x = random.randint(100, SCREEN_WIDTH - 100)
                self.wander_y = random.randint(100, SCREEN_HEIGHT - 100)
            
            if hasattr(self, 'wander_x'):
                self.player.move_towards(self.wander_x, self.wander_y)

    def render(self):
        # Draw background infrastructure
        self.city.draw(self.screen)

        # Hijackable Cars
        for car in self.cars:
            car.draw(self.screen)

        # NPCs
        for civ in self.civilians:
            civ.draw(self.screen)
            # Make civs roam around
            if self.timer % 80 == 0:
                civ.move_towards(civ.x + random.randint(-40, 40), civ.y + random.randint(-40, 40))

        # Enemy Squad Patrols
        for cop in self.cops:
            cop.draw(self.screen)

        # Particles & Explosions
        for p in self.particles:
            p.draw(self.screen)

        # Projectiles
        for b in self.bullets:
            b.draw(self.screen)

        # Playable character / Autonomous AI Agent
        self.player.draw(self.screen)

        # HUD Layer
        self.ui.draw_hud(
            self.screen, self.player, self.wanted_level, 
            self.mission_status, self.ai_agent_enabled, self.ai_objective, 
            self.bullets, self.cops, self.timer
        )

        pygame.display.flip()

if __name__ == "__main__":
    game = GameEngine()
    game.run()