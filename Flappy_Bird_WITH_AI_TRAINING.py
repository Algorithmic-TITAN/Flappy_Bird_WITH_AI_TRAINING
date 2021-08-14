import pygame
import os
import random
import time

def Game_one_frame(is_space_pressed):
  pygame.init()
  global bird
  global window
  global bird
  global wall
  global wall
  global cation_top_and_bottom
  global wall_up
  global distance_between_walls_VERTICAL
  global top_wall_coordinates
  global bottom_wall_coordinates
  global amount_of_passed_frames
  global gravity
  global bird_Y
  global first_play_in_run

  def blit_walls():
    for i in range(len(top_wall_coordinates)):
      window.blit(wall, bottom_wall_coordinates[i])
      window.blit(wall_up, top_wall_coordinates[i])

  def make_new_wall():
    how_much_up_wall_hole=random.randint(20,380)
    global top_wall_coordinates
    global bottom_wall_coordinates
    how_much_up1=(-1*how_much_up_wall_hole)
    how_much_up2=(-1*how_much_up_wall_hole+distance_between_walls_VERTICAL+wall.get_rect().size[1])
    top_wall_coordinates.append([900,how_much_up1])
    bottom_wall_coordinates.append([900, how_much_up2])

  def delete_walls():
    global top_wall_coordinates
    global bottom_wall_coordinates
    global wall
    if top_wall_coordinates[0][0]+wall.get_rect().size[0]<0:
      top_wall_coordinates.pop(0)
      bottom_wall_coordinates.pop(0)

  def move_walls():
    global top_wall_coordinates
    global bottom_wall_coordinates
    for i in range(len(top_wall_coordinates)):
      top_wall_coordinates[i][0]-=10
      bottom_wall_coordinates[i][0]-=10

  def do_all_with_walls():
    if round(amount_of_passed_frames/45, 0)==amount_of_passed_frames/45:
      make_new_wall()
    move_walls()
    blit_walls()
    delete_walls()

  def do_all_with_bird():
    global gravity
    global bird_Y
    gravity+=1.5
    if is_space_pressed:
      gravity=-15
    bird_Y+=round(gravity,0)

  def end_round():
    global bird
    global window
    global wall
    global cation_top_and_bottom
    global wall_up
    global distance_between_walls_VERTICAL
    global top_wall_coordinates
    global bottom_wall_coordinates
    global amount_of_passed_frames
    global gravity
    global bird_Y
    global first_play_in_run
    global round_ended_yet
    global crashed_birds
    global fitness_scores
    fitness_scores.append(amount_of_passed_frames)
    bird=pygame.image.load(os.path.join('download (12).png'))
    window=pygame.display.set_mode([900,550])
    bird=pygame.transform.scale(bird, [50,40])
    wall=pygame.image.load(os.path.join('download (9).png'))
    wall=pygame.transform.scale(wall, [wall.get_rect().size[0], wall.get_rect().size[1]*2])
    cation_top_and_bottom=pygame.image.load(os.path.join('download (10).png'))
    wall_up=pygame.transform.flip(wall, False, True)
    speed_button=pygame.image.load(os.path.join('download (13).png'))
    distance_between_walls_VERTICAL=250
    top_wall_coordinates=[]
    bottom_wall_coordinates=[]
    amount_of_passed_frames=0
    gravity=0
    bird_Y=250
    first_play_in_run=False
    round_ended_yet=True
    crashed_birds+=1

  def test_ENDGAME():
    global round_ended_yet
    round_ended_yet=False
    wall_X_SIZE, wall_Y_SIZE=wall.get_rect().size
    bird_X_SIZE, bird_Y_SIZE=bird.get_rect().size
    if bird_Y+bird_Y_SIZE>530:
      end_round()
    if bird_Y<20:
      end_round()
    for i in range(len(top_wall_coordinates)):
      #the first one is correct in the if statemen
      if not round_ended_yet:
        if 20>top_wall_coordinates[i][0]-10 and bird_X_SIZE+20<top_wall_coordinates[i][0]-10+wall_X_SIZE:
          blit_walls()
          if bird_Y>bottom_wall_coordinates[i][1] or bird_Y<top_wall_coordinates[i][1]+wall_Y_SIZE:
            end_round()

  if not amount_of_passed_frames==1:
    pygame.event.pump()
    keys_pressed=pygame.key.get_pressed()
    window.fill([0,0,0])
    window.fill([117,170,255])
    window.blit(cation_top_and_bottom, [0,-10])
    do_all_with_walls()
    do_all_with_bird()
    window.blit(bird, [20, bird_Y])
    window.blit(bird, [20, bird_Y])
    window.blit(cation_top_and_bottom, [0,-10])
    window.blit(pygame.transform.flip(cation_top_and_bottom, False, True), [0,530])
    window.blit(speed_button, [450,0])
    pygame.display.update()
    test_ENDGAME()
  amount_of_passed_frames+=1
  if amount_of_passed_frames==1:
    window.fill([0,0,0])
    window.fill([117,170,255])
    window.blit(cation_top_and_bottom, [0,-10])
    window.blit(bird, [20, bird_Y])
    window.blit(bird, [20, bird_Y])
    window.blit(cation_top_and_bottom, [0,-10])
    window.blit(pygame.transform.flip(cation_top_and_bottom, False, True), [0,530])
    window.blit(speed_button, [450,0])
    pygame.display.update()
    test_ENDGAME()
    if not first_play_in_run:
      make_new_wall()



def set_all_up_GAME():
  import pygame
  import os
  import random
  import time
  pygame.init()
  global bird
  global window
  global bird
  global wall
  global wall
  global cation_top_and_bottom
  global wall_up
  global distance_between_walls_VERTICAL
  global top_wall_coordinates
  global bottom_wall_coordinates
  global amount_of_passed_frames
  global gravity
  global bird_Y
  global first_play_in_run
  global speed_button
  bird=pygame.image.load(os.path.join('download (12).png'))
  window=pygame.display.set_mode([900,550])
  bird=pygame.transform.scale(bird, [50,40])
  wall=pygame.image.load(os.path.join('download (9).png'))
  wall=pygame.transform.scale(wall, [wall.get_rect().size[0], wall.get_rect().size[1]*2])
  cation_top_and_bottom=pygame.image.load(os.path.join('download (10).png'))
  wall_up=pygame.transform.flip(wall, False, True)
  distance_between_walls_VERTICAL=250
  top_wall_coordinates=[]
  bottom_wall_coordinates=[]
  amount_of_passed_frames=0
  gravity=0
  bird_Y=250
  first_play_in_run=True
  speed_button=pygame.image.load(os.path.join('download (13).png'))


def population_INIT_RANDOM():
  import random
  global full_population_weights
  global full_population_biases
  global weights_amount
  global weight_layers
  weights_amount=0
  weight_layers=[]
  population_element_WEIGHTS_HERE=[]
  population_element_BIASES_HERE=[]
  for i in range(len(layers)-1):
      weights_amount+=layers[i]*layers[i+1]
      weight_layers.append(layers[i]*layers[i+1])
  for i1 in range(population_size):
    population_element_WEIGHTS_HERE=[]
    population_element_BIASES_HERE=[]
    for i2 in range(weights_amount):
      population_element_WEIGHTS_HERE.append(random.uniform(-.1,.1))
      population_element_BIASES_HERE.append(random.uniform(-.1,.1))
    full_population_weights.append(population_element_WEIGHTS_HERE)
    full_population_biases.append(population_element_BIASES_HERE)

def SETUP_TRAINING():
  global generation_counter
  global population_size
  global layers
  global full_population_weights
  global full_population_biases
  global weight_layers
  global Full_mutation_rate_percent
  global partial_mutation_rate_percent
  global partial_mutation_rate_CHANGE_AMOUNT
  partial_mutation_rate_percent=50
  partial_mutation_rate_CHANGE_AMOUNT=0.2
  full_population_weights=[]
  Full_mutation_rate_percent=1
  full_population_biases=[]
  population_size=50
  layers=[10,12,8,10,12,10,8,15,1]
  generation_counter=0
  population_INIT_RANDOM()


def find_inputs():
    global INPUTS
    wall_size_X, wall_size_Y=wall.get_rect().size
    INPUTS=[]
    INPUTS.append(bird_Y) #player's y
    INPUTS.append(gravity) #basically player's y velocity
    #onto top wall coordinates
    INPUTS.append(top_wall_coordinates[0][0]+wall_size_X) #top wall's bottom right corner x coordinate
    INPUTS.append(top_wall_coordinates[0][0]) #top wall's bottom left corner x coordinate
    INPUTS.append(top_wall_coordinates[0][1]+wall_size_Y) #top wall's bottom right corner y coordinate
    INPUTS.append(top_wall_coordinates[0][1]+wall_size_Y) #top wall's bottom left corner y coordinate
    #now onto bottom wall
    INPUTS.append(bottom_wall_coordinates[0][0]+wall_size_X) #bottom wall's top right corner x coordinate
    INPUTS.append(bottom_wall_coordinates[0][0]) #bottom wall's top left corner x coordinate
    INPUTS.append(bottom_wall_coordinates[0][1]) #bottom wall's top right corner y coordinate
    INPUTS.append(bottom_wall_coordinates[0][1]) #top wall's top left corner y coordinate

def sigmoid(raw_num):
    import decimal
    global output
    decimal.getcontext().prec=50
    output=(1/(1+decimal.Decimal(2.71828)**(-1*(decimal.Decimal(round(raw_num[0], 5))))))

def run_network_ONE_FRAME(population_element):
    global output
    global all_edges_next_layer
    output=[]
    running_weights=full_population_weights[population_element]
    running_biases=full_population_biases[population_element]
    nodes_now=INPUTS
    nodes_now_LEN=len(INPUTS)
    weights_COUNTER_HERE=0
    for i1 in range(len(weight_layers)):
     all_edges_next_layer=[]
     for i3 in range(int(weight_layers[i1]/layers[i1])):
      first_node_next_layer=[]
      for i2 in range(int(weight_layers[i1]/layers[i1+1])):
          edge_value=nodes_now[i2]*running_weights[weights_COUNTER_HERE]
          edge_value+=running_biases[weights_COUNTER_HERE]
          weights_COUNTER_HERE+=1
          first_node_next_layer.append(edge_value)
      all_edges_next_layer.append(first_node_next_layer)
     nodes_now=[]
     for i in range(len(all_edges_next_layer)):
        add_up=0
        for i1 in range(len(all_edges_next_layer[i])):
            add_up+=all_edges_next_layer[i][i1]
        nodes_now.append(add_up)
    output=nodes_now
    sigmoid(output)

def decide_space():
    global ai_decided_space_pressed
    if output>0.5:
        ai_decided_space_pressed=True
    else:
        ai_decided_space_pressed=False

def display_speed_management():
    global display_speed
    global last_press_state
    #hold to put it at 60 fps
    pygame.event.pump()
    x, y=pygame.mouse.get_pos()
    if x>450 and y<100:
        if not pygame.mouse.get_pressed(3)[0]==last_press_state:
            display_speed=not display_speed
    last_press_state=display_speed

def find_fitnesses():
  global fitness_scores
  global crashed_birds
  crashed_birds=0
  fitness_scores=[]
  while crashed_birds<population_size:
      find_inputs()
      run_network_ONE_FRAME(crashed_birds)
      decide_space()
      Game_one_frame(ai_decided_space_pressed)
      display_speed_management()
      if display_speed==True:
          time.sleep(1/60)
      #This makes it so every element of the population has exactly one play to prove itself during the find_fitness() function.

def make_new_generation():
   #selection method commented is random weighted, the one being used is top 2
  #sum_fitness_scores=0
  #parent_choosing_list=[]
  #for i1 in range(len(fitness_scores)):
  #  for i2 in range(fitness_scores[i1]):
  #       parent_choosing_list.append(i1)
  #parent1_ID=parent_choosing_list[random.randint(0, len(parent_choosing_list)-1)]
  #parent2_ID=parent_choosing_list[random.randint(0, len(parent_choosing_list)-1)]
  best_parent1=0
  best_parent2=0
  for i1 in range(population_size):
      if fitness_scores[i1]>best_parent1:
          parent1_ID=i1
          best_parent1=fitness_scores[i1]
  for i2 in range(population_size):
      if fitness_scores[i2]>best_parent2 and not i2==parent1_ID:
          parent2_ID=i2
          best_parent2=fitness_scores[i2]
  parent1_weights=full_population_weights[parent1_ID]
  parent1_biases=full_population_biases[parent1_ID]
  parent2_weights=full_population_weights[parent2_ID]
  parent2_biases=full_population_biases[parent2_ID]
  for i3 in range(population_size):
      CHILD_WEIGHTS=[]
      CHILD_BIASES=[]
      for i4 in range(2):
       for i5 in range(weights_amount):
        if random.uniform(0,100)<=Full_mutation_rate_percent:
            if i4==0:
                CHILD_WEIGHTS.append(random.uniform(-.25, .25))
            else:
                CHILD_BIASES.append(random.uniform(-.25, .25))
        elif random.uniform(0,100)<=partial_mutation_rate_percent:
            if i4==0:
                if random.randint(1,2)==1:
                    CHILD_WEIGHTS.append(parent1_weights[i5]+random.uniform(-1*partial_mutation_rate_CHANGE_AMOUNT, partial_mutation_rate_CHANGE_AMOUNT))
                else:
                    CHILD_WEIGHTS.append(parent2_weights[i5]+random.uniform(-1*partial_mutation_rate_CHANGE_AMOUNT, partial_mutation_rate_CHANGE_AMOUNT))
            else:
                if random.randint(1,2)==1:
                    CHILD_BIASES.append(parent1_biases[i5]+random.uniform(-1*partial_mutation_rate_CHANGE_AMOUNT, partial_mutation_rate_CHANGE_AMOUNT))
                else:
                    CHILD_BIASES.append(parent2_biases[i5]+random.uniform(-1*partial_mutation_rate_CHANGE_AMOUNT, partial_mutation_rate_CHANGE_AMOUNT))
        else:
            if i4==0:
                if random.randint(1,2)==1:
                    CHILD_WEIGHTS.append(parent1_weights[i5])
                else:
                    CHILD_WEIGHTS.append(parent2_weights[i5])
            else:
                if random.randint(1,2)==1:
                    CHILD_BIASES.append(parent1_biases[i5])
                else:
                    CHILD_BIASES.append(parent2_biases[i5])
      full_population_weights.append(CHILD_WEIGHTS)
      full_population_biases.append(CHILD_BIASES)


def ARTIFICIAL_ADD_ONS():
  pass

def delete_previous_generation():
  for i in range(population_size):
      full_population_weights.pop(0)
      full_population_biases.pop(0)


def train_AI():
  global generation_counter
  find_fitnesses()
  make_new_generation()
  ARTIFICIAL_ADD_ONS()                              #THIS "ARTICICIAL_ADD-ONS" FUNCTION IS OPTINOAL
  delete_previous_generation()
  generation_counter+=1


SETUP_TRAINING()
set_all_up_GAME()
Game_one_frame(False)
display_speed=False

while True:
  pygame.event.pump()
  keys_pressed=pygame.key.get_pressed()
  train_AI()