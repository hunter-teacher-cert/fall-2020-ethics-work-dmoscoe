import random

# making a 2D array for the map filled with randomly placed 1's and 0's
def make_a_map(rows, cols):
  map = [[random.randint(0,1) for x in range(cols)] for y in range(rows)]
  return map

# displays the map
def show_map(map):
  district = 1
  for i in map:
    print('D{}:'.format(str(district)),i)
    district+=1

def show_district(map):
  district = int(input("What district would you like to display? "))
  print(map[district - 1]) #Districts begin with 1.

#Different results function
def display_results(map):
  results_table = []
  D = 1
  for district in map:
    results_dict = {0:0,1:0}
    for vote in district:
      if vote == 0:
        results_dict[0]+=1
      else:
        results_dict[1]+=1
    results_string = 'D{} results: {}'.format(D,results_dict)
    results_table.append(results_string)
    D+=1
  return results_table

def votes_vs_reps(map):
  """Assumes map is make_a_map(rows,cols). Prints the fraction of voters preferring 1, and the fraction of reps of party 1. Returns a list with these fractions."""

  OneReps = 0
  OneVoters = 0
  for district in map:
      if sum(district) > len(map[0]) / 2:
          OneReps += 1
      OneVoters += sum(district)
  FractionOneReps = OneReps / len(map)
  FractionOneVoters = OneVoters / (len(map[0]) * len(map))
  print(f'The fraction of One voters is about {FractionOneVoters:.2f}.')
  print(f'The fraction of One reps is about {FractionOneReps:.2f}.')
    
  return [FractionOneReps, FractionOneVoters]

#NEW METHODS FROM DANIEL ON 11/22

def DoVotersWinDistrict(voters,district):
    """voters is an entry in voterlocs.txt. District is an entry in districts.txt. Returns True if district contains at least 2 voters. Returns False otherwise."""
    VotersInDistrict = 0
    for voter in voters:
        if voter in district:
            VotersInDistrict += 1
    
    return VotersInDistrict > 1

def DistrictsWonByState(voters,districts):
    """voters is an entry in voterlocs.txt. districts is the entire list districts.txt. Returns a list where list[i] = j means that voters won j districts in state i."""
    DistrictsWonByState = []
    for i in range(170):
        DistrictsWonByState.append(0)
    
    for district in districts:
        if DoVotersWinDistrict(voters,district):
            DistrictsWonByState[district[0] - 1] += 1
    
    return DistrictsWonByState

def MakeHistogram(voters,districts):
    """voters is an entry in voterlocs.txt. districts is the entire list districts.txt. Returns a histogram where histogram[i] = j means that voters won i districts in j states. Sum(j) = 170."""
    histogram = [0,0,0,0]
    
    for entry in DistrictsWonByState(voters,districts):
        histogram[entry] += 1
    
    return histogram

def StatesWithNDistrictsWon(voters,districts,n):
    """voters is an entry in voterlocs.txt. districts is the entire list districts.txt. Returns a list of states for which voters won n districts."""
    
    a = DistrictsWonByState(voters,districts)
    StatesWithNDistrictsWon = []
    
    for i in range(len(a)):
        if a[i] == n:
            StatesWithNDistrictsWon.append(i)
    
    return StatesWithNDistrictsWon

#~~~~~~Main~~~~~#
rows = int(input("How many rows are on this map? "))
cols = int(input("How many columns are on this map? "))
print('\nThe map:')
map = make_a_map(rows,cols)
show_map(map)
results_table = display_results(map)
print('\nHere are the results:')
for i in results_table:
  print(i)
print('\nHere is the fraction of who voted for which candidate:')
votes_vs_reps(map)

#map = [[1, 0, 0,], [0, 1, 1], [1, 1, 0]]
#show_district(map)
#print(results(map))
#fair_representation(results(map))